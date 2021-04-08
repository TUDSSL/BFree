#!/bin/bash

SIZE_X=3
SIZE_Y=1.8
OUTDIR="output"
DATADIR="data"

export PYTHONPATH=$PYTHONPATH:"../"

# The python -> C comparison (bit special, no csv. Data is direcly in the python file
python plot_bfree_boot.py
