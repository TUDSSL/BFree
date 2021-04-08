#include "debug.h"

#if !(DEBUG_USE_CIO)
void uartConfig(void) {
    // Pins, 2.1/UCA0RXD (to MCU), 2.0/UCA0TXD (from MCU)
    P2REN = 0;                                              // Disable pull up/down down registers

    //Select UART peripheral
    P2SEL1 |= (BIT1 | BIT0);
    P2SEL0 &= ~(BIT1 | BIT0);

    // Configure USCI_A0 for UART mode
    UCA0CTLW0 = UCSWRST;                                    // Put eUSCI in reset
    UCA0CTLW0 |= UCSSEL_2;                                  // SMCLK as clock source
    UCA0BRW = 104;
    //UCA0BR1 = 0x00;
    UCA0MCTLW |= UCOS16 | 0x0020 | 0xD600;
    UCA0CTLW0 &= ~UCSWRST;                                  // Initialize eUSCI
}

int io_putchar(int c) {
    while (!(UCA0IFG&UCTXIFG));                             // Check if USCI_A0 TX buffer ready?
    UCA0TXBUF = c;
    return 0;
}

int io_puts_no_newline(const char *str) {
  uint8_t len_str = strlen(str);
  volatile uint8_t i;
  for(i=0;i<len_str;i++) {
    while (!(UCA0IFG&UCTXIFG));                             // Check if USCI_A0 TX buffer ready?
    UCA0TXBUF = str[i];
  }
  return 0;
}
#endif /* !DEBUG_USE_CIO */
