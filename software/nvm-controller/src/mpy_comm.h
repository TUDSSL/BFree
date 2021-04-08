#ifndef MPY_COMM_H__
#define MPY_COMM_H__

#include <stdlib.h>
#include <msp430.h>

void mpy_comm_init(void);
void mpy_comm_start(void);
int mpy_write(char *src, size_t size);
int mpy_read(char *dst, size_t size);

/* Fast writing */
int mpy_write_dma(char *src, size_t size);
int mpy_write_dma_blocking(char *src, size_t size);

int mpy_read_dma(char *dst, size_t size);
int mpy_read_dma_blocking(char *dst, size_t size);

// SPI port 5
#define SPI_MOSI BIT0   // P5.0
#define SPI_MISO BIT1   // P5.1
#define SPI_SCLK BIT2   // P5.2
#define SPI_SC   BIT3   // P5.3

#define WR_PIN BIT7

/* We don't use the RD pin defined on the PCB, so repurpose it as a reset pin */
#define RD_PIN BIT6
#define RST_PIN RD_PIN

/* Pin connected to a checkpoint clear button (button press pulls low) */
#define CHECKPOINT_CLR_PIN  BIT6 // P4.6

/* Use pin interrupt to reset the board (not connected to the actual reset pin) */
#define RST_PIN_ISR (0)

static inline void mpy_wr_high(void)
{
    P1OUT |= WR_PIN;
}

static inline void mpy_wr_low(void)
{
    P1OUT &= ~WR_PIN;
}

static inline int mpy_cs(void)
{
    if (P5IN & SPI_SC) {
        return 1;
    }
    return 0;
}

static inline void mpy_wait_cs(void)
{
    while (mpy_cs() != 0);
}

static inline char mpy_write_byte(char data)
{
    mpy_wait_cs();

    UCB1TXBUF = data;
    mpy_wr_high();
    while(!(UCB1IFG & UCTXIFG));
    UCB1IFG &= ~UCTXIFG;
    mpy_wr_low();

    // Also clear the read IF (discard)
    UCB1IFG &= ~UCRXIFG;
    while(!(UCB1IFG & UCRXIFG));
    data = UCB1RXBUF;
    UCB1IFG &= ~UCRXIFG;

    UCB1TXBUF = 0;

    return data;
}

static inline char mpy_read_byte(void)
{
    mpy_wait_cs();

    mpy_wr_high();
    while(!(UCB1IFG & UCRXIFG));
    mpy_wr_low();
    char data = UCB1RXBUF;
    UCB1IFG &= ~UCRXIFG;

    // Alsoc clear the write IF (discard)
    UCB1IFG &= ~UCTXIFG;

    return data;
}

/*
 * return  1 = button pressed, 0 = button not pressed
 */
static inline int mpy_checkpoint_clear_state(void)
{
    if (P4IN & CHECKPOINT_CLR_PIN) {
        return 0;
    }
    return 1;
}

#endif /* MPY_COMM_H__ */
