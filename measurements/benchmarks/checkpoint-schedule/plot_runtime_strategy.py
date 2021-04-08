import argparse
import sys
import os

import barplotter
import plotcolor

parser = argparse.ArgumentParser(description='Generate computation benchmark figure')
parser.add_argument("data", help=".csv file containing the data")
parser.add_argument("outfile", help=".csv file containing the data")
parser.add_argument("--size_x", help="The figure x size (default: auto)")
parser.add_argument("--size_y", help="The figure y size (default: auto)")

args = parser.parse_args()
data_file = args.data
out_file = args.outfile

figsize_x = args.size_x
figsize_y = args.size_y
if figsize_x != None and figsize_y != None:
    figsize = (float(figsize_x), float(figsize_y))
else:
    figsize = None

print('Data file:', data_file)
print('Output file', out_file)
print('Figure size', figsize)

bars = []
yaxis = []
xaxis = []

bars.append({
    'name': 'Fibonacci execution time',
    'field': 'runtime',
    'color': plotcolor.LBLUE,
    'type': 'float',
    'mult': 0.001,
    'idx': None,
    'data': []
    })

yaxis.append({
    'key': 'time',
    'name': 'Execution time (s)',
    'data': []
    })

xaxis.append({
    'key': '',
    'name': 'Checkpoint strategy',
    'type': 'float',
    'format': '${:.1f}$',
    'data': [0, 1, 2],
    'labels': ['Period', 'Trigger', 'Hybrid']
    })


barplotter.plot(xaxis, yaxis, bars, data_file, out_file, figsize=figsize)

