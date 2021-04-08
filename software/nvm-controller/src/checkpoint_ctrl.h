#ifndef CHECKPOINT_CTRL_H__
#define CHECKPOINT_CTRL_H__

#include <stdint.h>

#include "checkpoint.h"

/*
 * One byte commands
 */
#define CPCMND_REQUEST_CHECKPOINT   'x'
#define CPCMND_REQUEST_RESTORE      'y'
#define CPCMND_SEGMENT              's'
#define CPCMND_REGISTERS            'r'
#define CPCMND_ACK                  'a'
#define CPCMND_CONTINUE             'c'
#define CPCMND_DEL                  'd'

typedef enum process_state {
    PS_COMMAND,
    PS_CHECKPOINT,
    PS_CHECKPOINT_SEGMENT,
    PS_CHECKPOINT_REGISTERS,
    PS_PRESTORE,
    PS_PRESTORE_SEGMENT,
    PS_PRESTORE_REGISTERS,
    PS_ERROR
} process_state_t;

void process_error(process_state_t state);

void process_reboot_sync(void);

void process_dispatch(void);
void process_command_byte(uint8_t byte);

void process_checkpoint_command(void);
void process_checkpoint_segment(void);
void process_checkpoint_registers(void);

void process_restore_command(void);
void process_restore_segment(segment_t *segment);
void process_restore_registers(segment_t *segment);

void process_delete_checkpoint(void);

#endif /* CHECKPOINT_CTRL_H__ */
