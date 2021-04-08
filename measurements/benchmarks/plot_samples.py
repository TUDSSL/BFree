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
parser.add_argument("--bar_width", help="The figure bar width size (default: auto)")

args = parser.parse_args()
data_file = args.data
out_file = args.outfile
bar_width = args.bar_width

figsize_x = args.size_x
figsize_y = args.size_y
if figsize_x != None and figsize_y != None:
    figsize = (float(figsize_x), float(figsize_y))
else:
    figsize = None

if bar_width == None:
    bar_width = 0.3
else:
    bar_width = float(bar_width)

print('Data file:', data_file)
print('Output file', out_file)
print('Figure size', figsize)

bars = []
yaxis = []
xaxis = []

bars.append({
    'key': 'total_samples',
    'name': 'Total sample count',
    'field': "total samples",
    'color': plotcolor.LORANGE,
    'type': 'float',
    #'mult': 0.001,
    'idx': None,
    'data': []
    })

yaxis.append({
    'key': 'count',
    'name': 'Occurrences',
    'data': []
    })

xaxis.append({
    'key': 'duty_cycle',
    'name': 'Duty cycle (\%) of 6 seconds',
    'field': 'Duty Cycle',
    'type': 'float',
    'format': '${:.1f}$',
    'data': []
    })


if bar_width != None:
    barplotter.plot(xaxis, yaxis, bars, data_file, out_file, figsize=figsize, bar_width=bar_width)
else:
    barplotter.plot(xaxis, yaxis, bars, data_file, out_file, figsize=figsize)

