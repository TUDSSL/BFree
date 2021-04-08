#!/bin/bash

SIZE_X=3
SIZE_Y=1.8
OUTDIR="output"
DATADIR="data"

export PYTHONPATH=$PYTHONPATH:"../"

python plot_runtime.py "$DATADIR/Fibonacci csv line.csv" "$OUTDIR/runtime_duty_cycle_fibonacci.pdf" --size_x $SIZE_X --size_y $SIZE_Y
python plot_runtime.py "$DATADIR/Bitcount csv line.csv" "$OUTDIR/runtime_duty_cycle_bitcount.pdf" --size_x $SIZE_X --size_y $SIZE_Y
python plot_runtime.py "$DATADIR/Strlen csv line.csv" "$OUTDIR/runtime_duty_cycle_strlen.pdf" --size_x $SIZE_X --size_y $SIZE_Y

python plot_restores.py "$DATADIR/Fibonacci csv line.csv" "$OUTDIR/restores_duty_cycle_fibonacci.pdf" --size_x $SIZE_X --size_y $SIZE_Y
python plot_restores.py "$DATADIR/Bitcount csv line.csv" "$OUTDIR/restores_duty_cycle_bitcount.pdf" --size_x $SIZE_X --size_y $SIZE_Y
python plot_restores.py "$DATADIR/Strlen csv line.csv" "$OUTDIR/restores_duty_cycle_strlen.pdf" --size_x $SIZE_X --size_y $SIZE_Y

python plot_runtime.py "$DATADIR/LoRa csv line.csv" "$OUTDIR/runtime_duty_cycle_lora.pdf" --size_x 2.3 --size_y 1.8
python plot_runtime.py "$DATADIR/E-Paper csv line.csv" "$OUTDIR/runtime_duty_cycle_epaper.pdf" --size_x 2.3 --size_y 1.8

python plot_samples.py "$DATADIR/LoRa csv line.csv" "$OUTDIR/samples_duty_cycle_lora.pdf" --size_x 2 --size_y 1.8
python plot_samples.py "$DATADIR/E-Paper csv line.csv" "$OUTDIR/samples_duty_cycle_epaper.pdf" --size_x 2 --size_y 1.8 #--bar_width 0.4

python plot_restores.py "$DATADIR/LoRa csv line.csv" "$OUTDIR/restores_duty_cycle_lora.pdf" --size_x 2.3 --size_y 1.8
python plot_restores.py "$DATADIR/E-Paper csv line.csv" "$OUTDIR/restores_duty_cycle_epaper.pdf" --size_x 2.3 --size_y 1.8

# The python -> C comparison (bit special, no csv. Data is direcly in the python file
python plot_c_vs_cpy_vs_bfree.py "$OUTDIR/benchmark_c_vs_cpy_vs_bfree.pdf" --size_x 4.8 --size_y 2
