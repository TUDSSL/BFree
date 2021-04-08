#!/bin/bash

OUTDIR="output"
DATADIR="data"

export PYTHONPATH=$PYTHONPATH:"../"

BASENAME="one-checkpoint-3k-lux-1500uf"

python process_one_checkpoint_run.py "$DATADIR/3klux-1500uF-1-cp-normal-200_200.csv" -o "$OUTDIR/$BASENAME-periodic-200ms-200ms.pdf" -l "$OUTDIR/one-checkpoint-legend.pdf"
python process_one_checkpoint_run.py "$DATADIR/3klux-1500uF-1-cp-normal-100_100.csv" -o "$OUTDIR/$BASENAME-periodic-100ms-100ms.pdf"

python process_one_checkpoint_run.py "$DATADIR/3klux-1500uF-1-cp-trigger-0_200.csv" -o "$OUTDIR/$BASENAME-trigger-0ms-200ms.pdf"
python process_one_checkpoint_run.py "$DATADIR/3klux-1500uF-1-cp-trigger-0_100.csv" -o "$OUTDIR/$BASENAME-trigger-0ms-100ms.pdf"

python process_one_checkpoint_run.py "$DATADIR/3klux-1500uF-1-cp-hybrid-200_100.csv" -o "$OUTDIR/$BASENAME-hybrid-200ms-100ms.pdf"
python process_one_checkpoint_run.py "$DATADIR/3klux-1500uF-1-cp-hybrid-300_100.csv" -o "$OUTDIR/$BASENAME-hybrid-300ms-100ms.pdf"
