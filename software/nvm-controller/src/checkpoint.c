#include <stdlib.h>
#include <string.h>

#include "nvm.h"
#include "checkpoint.h"

NVM volatile uint16_t checkpoint_active_base_idx = 0; // atomic

/*
 * Non-volatile tables holding the segments in a checkpoint
 * Array of segment pointers
 * TODO: The segments can be made a linked list
 */
#define CHECKPOINT_MAX_SEGMENTS 16
NVM segment_t *checkpoint_table_a[CHECKPOINT_MAX_SEGMENTS];
NVM segment_t *checkpoint_table_b[CHECKPOINT_MAX_SEGMENTS];

/*
 * Defined in the linkerscript, devides the non-volatile memory in two
 * The checkpoint should be double buffered
 */
extern uint32_t _checkpoint_base_a;
extern uint32_t _checkpoint_base_b;

uint32_t *checkpoint_working_base;
uint32_t *checkpoint_restore_base; // The segments used

segment_t **checkpoint_working_table;
segment_t **checkpoint_restore_table;

uint16_t checkpoint_table_idx;

char *checkpoint_working_end_allocated;

void checkpoint_update(void)
{
    if (checkpoint_active_base_idx == 0) {
        /* Set the base for the segments */
        checkpoint_working_base = &_checkpoint_base_a;
        checkpoint_restore_base = &_checkpoint_base_b;

        /* Set the active segment table */
        checkpoint_working_table = checkpoint_table_a;
        checkpoint_restore_table = checkpoint_table_b;
    } else {
        /* Set the base for the segments */
        checkpoint_working_base = &_checkpoint_base_b;
        checkpoint_restore_base = &_checkpoint_base_a;

        /* Set the active segment table */
        checkpoint_working_table = checkpoint_table_b;
        checkpoint_restore_table = checkpoint_table_a;
    }

    // Set the end of the allocated memory
    checkpoint_working_end_allocated = (char *)checkpoint_working_base;

    // Clear the current table
    checkpoint_table_clear_working();
    checkpoint_table_idx = 0;
}

void checkpoint_table_clear_working(void)
{
    memset(checkpoint_working_table, 0, (sizeof(segment_t *) * CHECKPOINT_MAX_SEGMENTS));
}

void checkpoint_table_clear_restore(void)
{
    memset(checkpoint_restore_table, 0, (sizeof(segment_t *) * CHECKPOINT_MAX_SEGMENTS));
}

void checkpoint_table_clear_all(void)
{
    for (int i=0; i<CHECKPOINT_MAX_SEGMENTS; i++) {
        checkpoint_table_a[i] = NULL;
        checkpoint_table_b[i] = NULL;
    }
}

void checkpoint_table_add(segment_t *segment)
{
    // TODO: add size checking
    checkpoint_working_table[checkpoint_table_idx++] = segment;
}

segment_t *checkpoint_segment_alloc(size_t size)
{
    segment_t *seg;
    seg = (segment_t *)checkpoint_working_end_allocated;

    /* Adjust size to be 16-bit aligned */
    size = (size % 2) ? size + 1 : size;

    /* Total size = size of the meta data + size of the segment data */
    size = size + sizeof(segment_meta_t);
    checkpoint_working_end_allocated = &checkpoint_working_end_allocated[size];

    /* Register the segment in the table */
    checkpoint_table_add(seg);

    return seg;
}

void checkpoint_commit(void)
{
    /* Go the the other buffer */
    if (checkpoint_active_base_idx == 0) {
        checkpoint_active_base_idx = 1;
    } else {
        checkpoint_active_base_idx = 0;
    }
    //__asm__ volatile("": : :"memory"); // Memory barrier TODO: Need this?

    checkpoint_update();
}

void checkpoint_get_segment_iter(segment_iter_t *segment_iter)
{
    segment_iter->segment = checkpoint_restore_table[0];
    segment_iter->idx = 0;
}

int checkpoint_get_next_segment(segment_iter_t *segment_iter)
{
    size_t new_idx = segment_iter->idx + 1;
    segment_t *seg = checkpoint_restore_table[new_idx];

    segment_iter->segment = seg;
    segment_iter->idx = new_idx;

    if (seg == NULL) {
        // No other segment
        return 0;
    }
    return 1;
}
