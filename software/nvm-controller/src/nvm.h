#ifndef NVM_H__
#define NVM_H__

/* Declare a NVM variable */
//#define NVM __attribute__ ((persistent))
#define NVM __attribute__((section(".persistent")))

#endif /* NVM_H__ */
