import argparse
import sys
import os

import barplotter
import plotcolor

parser = argparse.ArgumentParser(description='Generate computation benchmark figure')
parser.add_argument("outfile", help=".csv file containing the data")
parser.add_argument("--size_x", help="The figure x size (default: auto)")
parser.add_argument("--size_y", help="The figure y size (default: auto)")

args = parser.parse_args()
out_file = args.outfile

figsize_x = args.size_x
figsize_y = args.size_y
if figsize_x != None and figsize_y != None:
    figsize = (float(figsize_x), float(figsize_y))
else:
    figsize = None

print('Output file', out_file)
print('Figure size', figsize)

bars = []
yaxis = []
xaxis = []

bars.append({
    'name': 'C',
    'color': plotcolor.LORANGE,
    'type': 'float',
    #'mult': 0.001,
    'idx': None,
    'data': [8.4918, 5.2905, 1.422]
    })

bars.append({
    'name': 'Vanilla CPy',
    'color': plotcolor.DBLUE,
    'type': 'float',
    #'mult': 0.001,
    'idx': None,
    'data': [1407.97, 4224.52, 1584.24]
    })

bars.append({
    'name': 'BFree (trigger)',
    'color': plotcolor.DGREEN,
    'type': 'float',
    #'mult': 0.001,
    'idx': None,
    'data': [1674.9, 4537.1, 1560.066667]
    })

bars.append({
    'name': 'BFree (periodic)',
    'color': plotcolor.LGREEN,
    'type': 'float',
    #'mult': 0.001,
    'idx': None,
    'data': [2520.166667, 7066.2, 2481.9]
    })

yaxis.append({
    'key': 'time',
    'name': 'Time ($\mu$s)',
    'data': []
    })

xaxis.append({
    'key': '',
    'name': None,
    'type': 'float',
    'format': '${:.1f}$',
    'data': [0, 1, 2],
    'labels': ['Fibonacci', 'String length', 'Bit count']
    })


barplotter.plot(xaxis, yaxis, bars, None, out_file, figsize=figsize, yscale='log', bar_width=0.15)

