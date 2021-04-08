#ifndef PORTS_C_
#define PORTS_C_

#include "ports.h"

void portConfig(void)
{
    //P1DIR = 0;                                              // Set P1 to input
    //P1REN = 0xFF;                                           // To enable pull up/down resistors for all 8 bits of P1
    //P1OUT = 0;                                              //  Pull down enable

    //P2OUT = 0;
    //P2DIR = 0xFF;
    //P2REN = 0;

    P3DIR = 0;
    P3REN = 0xFF;
    P3OUT = 0;

    //P4DIR = 0;
    //P4REN = 0xFF;
    //P4OUT = 0;

    //P5DIR = 0;
    //P5REN = 0xFF;
    //P5OUT = 0;

    //P6DIR = 0;
    //P6REN = 0xFF;
    //P6OUT = 0;

    //P7DIR = 0;
    //P7REN = 0xFF;
    //P7OUT = 0;

    //P8DIR = 0;
    //P8REN = 0xFF;
    //P8OUT = 0;

    //PJDIR = 0;
    //PJREN = 0xFF;
    //PJOUT = 0;

    WDTCTL = WDTPW | WDTHOLD;               // Stop watchdog timer
    PM5CTL0 &= ~LOCKLPM5;                   // Clear the LOCKLPM5 bit in the PM5CTL0 register
}

void clockConfig(void)
{
    // Configure one FRAM waitstate as required by the device datasheet for MCLK
    // operation beyond 8MHz _before_ configuring the clock system.
    FRCTL0 = FRCTLPW | NWAITS_1;

    // Clock System Setup
    CSCTL0_H = CSKEY_H;                     // Unlock CS registers
    CSCTL1 = DCOFSEL_0;                     // Set DCO to 1MHz

    // Set SMCLK = MCLK = DCO, ACLK = VLOCLK
    CSCTL2 = SELA__VLOCLK | SELS__DCOCLK | SELM__DCOCLK;

    // Per Device Errata set divider to 4 before changing frequency to
    // prevent out of spec operation from overshoot transient
    CSCTL3 = DIVA__4 | DIVS__4 | DIVM__4;   // Set all corresponding clk sources to divide by 4 for errata
    CSCTL1 = DCOFSEL_4 | DCORSEL;           // Set DCO to 16MHz

    // Delay by ~10us to let DCO settle. 60 cycles = 20 cycles buffer + (10us / (1/4MHz))
    __delay_cycles(60);
    CSCTL3 = DIVA__1 | DIVS__1 | DIVM__1;   // Set all dividers to 1 for 16MHz operation
    CSCTL0_H = 0;                           // Lock CS registers
}

void ledConfig(void)
{
    P1OUT &= ~BIT0;
    P1DIR |= BIT0;                                          // Set P1.0 / LED1 to output direction (BIT0)

    P1OUT &= ~BIT1;
    P1DIR |= BIT1;                                          // Set P1.1 / LED2 to output direction (BIT1)
}


#endif /* PORTS_C_ */
