#!/bin/bash

SIZE_Y=1.8
OUTDIR="output"
DATADIR="data"

export PYTHONPATH=$PYTHONPATH:"../:../../"

python plot_runtime_strategy.py "$DATADIR/Fibonacci checkpoint strategy.csv" "$OUTDIR/runtime_strategy_fibonacci-3klux-15mF.pdf" --size_x 2.5 --size_y $SIZE_Y

python plot_restores_strategy.py "$DATADIR/Fibonacci checkpoint strategy.csv" "$OUTDIR/restores_strategy_fibonacci-3klux-15mF.pdf" --size_x 3 --size_y $SIZE_Y
