#ifndef CHECKPOINT_H__
#define CHECKPOINT_H__

#include <stdlib.h>
#include <stdint.h>

typedef uint32_t segment_size_t;
typedef uint8_t registers_size_t;

typedef enum segment_type {
    SEGMENT_TYPE_MEMORY,
    SEGMENT_TYPE_REGISTERS
} segment_type_t;

typedef struct segment_meta {
    segment_type_t type;
    segment_size_t addr_start;
    segment_size_t addr_end;
    segment_size_t size;
} segment_meta_t;

typedef struct segment {
    segment_meta_t meta;
    char data[];
} segment_t;

typedef struct segment_iter {
    segment_t *segment;
    size_t idx;
} segment_iter_t;

segment_t *segment_alloc(size_t size);

void checkpoint_update(void);
void checkpoint_table_clear_working(void);
void checkpoint_table_clear_restore(void);
void checkpoint_table_clear_all(void);
void checkpoint_table_add(segment_t *segment);
segment_t *checkpoint_segment_alloc(size_t size);
void checkpoint_commit(void); // Finish a checkpoint
void checkpoint_get_segment_iter(segment_iter_t *segment_iter);
int checkpoint_get_next_segment(segment_iter_t *segment_iter);

#endif /* CHECKPOINT_H__ */
