#ifndef DEBUG_H_
#define DEBUG_H_

// TODO move to somewhere in CMake
#define DEBUG_PRINT     (0)
#define DEBUG_USE_CIO   (1)

#if !(DEBUG_USE_CIO)

#include<msp430.h>
#include<string.h>
#include<stdint.h>

void uartConfig(void);
int io_putchar(int);
int io_puts_no_newline(const char *);
void printf(char *, ...);                                   // tiny printf function

#endif /* !DEBUG_USE_CIO */

#if DEBUG_PRINT
#define DBG_PRINT printf
#else
#define DBG_PRINT(...)
#endif

#endif /* DEBUG_H_ */
