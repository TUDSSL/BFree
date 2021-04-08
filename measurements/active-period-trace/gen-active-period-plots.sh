#!/bin/bash

OUTDIR="output"
DATADIR="data"

export PYTHONPATH=$PYTHONPATH:"../"

python process_active_period_run.py "$DATADIR/1klux-1500uF-90sec.csv" -o "$OUTDIR/active-period-1k-lux.pdf"
python process_active_period_run.py "$DATADIR/3klux-1500uF-90sec.csv" -o "$OUTDIR/active-period-3k-lux.pdf"
