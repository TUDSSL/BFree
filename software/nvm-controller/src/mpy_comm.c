#include <msp430.h>
#include "eusci_b_spi.h"

#include "mpy_comm.h"


#define CHECK_SIZE(size_) do {  \
    if (size_ == 0) return 1;   \
} while (0)

void mpy_comm_init(void)
{
    /* Initialize the checkpoint clear button */
    P4DIR &= ~CHECKPOINT_CLR_PIN; // Set button as input
    P4OUT |= CHECKPOINT_CLR_PIN; // Set to pullup
    P4REN |= CHECKPOINT_CLR_PIN; // Enable pullup

    /* Select SPI functionality for the pins */
    P5SEL1 &= ~(SPI_MOSI | SPI_MISO | SPI_SCLK);
    P5SEL0 |= (SPI_MOSI | SPI_MISO | SPI_SCLK);

    /* Initialize the WR pin to signal when the MSP is done processing */
    P1OUT &= ~WR_PIN;
    P1DIR |= WR_PIN;

#if RST_PIN_ISR
    /* Initialize the Reset signal pin as input */
    P1DIR &= ~RST_PIN;
    P1REN |= RST_PIN; // Enable pulldown
    P1IES &= ~RST_PIN; // Rising edge 0 -> 1
    P1IFG &= ~RST_PIN; // Clear interrupt flag
    P1IE |= RST_PIN; // Enable interrupt
#endif

    P5DIR &= ~SPI_SC; // Set CS as input
}

void mpy_comm_start(void)
{
    /* Configure SPI */
    EUSCI_B_SPI_initSlaveParam param;
    param.msbFirst = EUSCI_B_SPI_MSB_FIRST;
    param.clockPhase = EUSCI_B_SPI_PHASE_DATA_CAPTURED_ONFIRST_CHANGED_ON_NEXT;
    param.clockPolarity = EUSCI_B_SPI_CLOCKPOLARITY_INACTIVITY_LOW;
    param.spiMode = EUSCI_B_SPI_3PIN;

    EUSCI_B_SPI_initSlave(EUSCI_B1_BASE, &param);
    EUSCI_B_SPI_enable(EUSCI_B1_BASE);
    EUSCI_B_SPI_clearInterrupt(EUSCI_B0_BASE,
            EUSCI_B_SPI_RECEIVE_INTERRUPT);

    //mpy_wr_low();
    //mpy_wr_high();
    //__delay_cycles(100);
    //mpy_wr_low();
}

int mpy_write(char *src, size_t size)
{
    CHECK_SIZE(size);

    for (size_t i=0; i<size; i++) {
        mpy_write_byte(src[i]);
    }

    return 0;
}

int mpy_read(char *dst, size_t size)
{
    CHECK_SIZE(size);

    for (size_t i=0; i<size; i++) {
        dst[i] = mpy_read_byte();
    }

    return 0;
}

int mpy_write_dma(char *src, size_t size)
{
    mpy_wait_cs();

    DMACTL1 = DMA3TSEL__UCB1TXIFG;  // UCB1TXIFG if DMA Channel 3

    __data16_write_addr((intptr_t) &DMA3SA,(intptr_t) src);
    __data16_write_addr((intptr_t) &DMA3DA,(intptr_t) &UCB1TXBUF);

    DMA3SZ = size;
    DMA3CTL = DMADT_0 | DMASRCINCR_3 | DMADSTBYTE__BYTE | DMASRCBYTE__BYTE | DMAEN;

    mpy_wr_high();

    // Trigger transfer
    UCB1IFG &= ~UCTXIFG;
    UCB1IFG |=  UCTXIFG;

    return 0;
}

int mpy_write_dma_blocking(char *src, size_t size)
{
    int ret = mpy_write_dma(src, size);
    while (!(DMA3CTL & DMAIFG)); // Wait for DMA to finish
    mpy_wr_low();

    // Also clear the read IF (discard)
    UCB1IFG &= ~UCRXIFG;
    while(!(UCB1IFG & UCRXIFG));
    UCB1IFG &= ~UCRXIFG;
    while(!(UCB1IFG & UCRXIFG));
    volatile char data = UCB1RXBUF;
    (void)data;
    UCB1IFG &= ~UCRXIFG;
    UCB1TXBUF = 0;

    return ret;
}

int mpy_read_dma(char *dst, size_t size)
{
    mpy_wait_cs();

    DMACTL1 = DMA3TSEL__UCB1RXIFG;  // UCB1RXIFG if DMA Channel 3

    __data16_write_addr((intptr_t) &DMA3SA,(intptr_t) &UCB1RXBUF);
    __data16_write_addr((intptr_t) &DMA3DA,(intptr_t) dst);

    DMA3SZ = size;
    DMA3CTL = DMADT_0 | DMADSTINCR_3 | DMADSTBYTE__BYTE | DMASRCBYTE__WORD | DMAEN;

    mpy_wr_high();

    // Trigger transfer
    //UCB1IFG &= ~UCTXIFG;
    //UCB1IFG |=  UCTXIFG;

    return 0;
}

int mpy_read_dma_blocking(char *dst, size_t size)
{
    int ret = mpy_read_dma(dst, size);
    while (!(DMA3CTL & DMAIFG)); // Wait for DMA to finish
    mpy_wr_low();

    return ret;
}

#if RST_PIN_ISR
__attribute__((interrupt(PORT1_VECTOR)))
void port1_isr(void)
{
    if (P1IFG & RST_PIN) {
        P1IFG &= ~RST_PIN; // clear flag

        /* Reset the system */
        PMMCTL0 |= PMMSWBOR;
    }
}
#endif
