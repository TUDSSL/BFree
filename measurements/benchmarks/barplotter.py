import argparse
import sys
import csv
import os
import numpy as np

import statistics as stat
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import ticker

import plotcolor
import plotstyle

def plot(xaxis, yaxis, bars, data_file, out_file, figsize, bar_width = 0.3, bar_pad = 0.03, yscale='linear'):
    def process(csv_file):

        fields = None

        def init_map(imap, fields):
            for m in imap:
                try:
                    m['idx'] = fields.index(m['field'])
                except:
                    pass


        def fill_map(fmap, row):
            for m in fmap:
                try:
                    d = row[m['idx']]
                except:
                    continue

                try:
                    if m['type'] == 'float':
                        d = float(d)
                except:
                    pass
                try:
                    d = d * m['mult']
                except:
                    pass

                m['data'].append(d)


        # Parse csv
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            got_fields = False
            for row in reader:
                #print('Row:', row)
                if got_fields == False:
                    fields = [r.strip() for r in row]
                    got_fields = True
                    init_map(bars, fields)
                    init_map(xaxis, fields)
                    init_map(yaxis, fields)
                else:
                    row = [r.strip() for r in row]
                    fill_map(bars, row)
                    fill_map(xaxis, row)
                    fill_map(yaxis, row)

        print('Fields:', fields)
        print('Bars:', bars)
        print('x-axis:', xaxis)
        print('y-axis:', yaxis)
        return

    if data_file != None:
        process(data_file)

    plotstyle.set_style()

    fig, ax = plt.subplots(figsize=figsize)

    ax.xaxis.grid(False)
    ax.yaxis.grid(True)
    ax.tick_params(axis='x', which='minor', bottom=False)

    n_groups = len(bars[0]['data'])
    n_per_group = len(bars)

    bar_idx = []
    for b in range(n_per_group):
        r = np.arange(n_groups)
        ro = [x + (bar_width+bar_pad) * (b+1) for x in r]
        bar_idx.append(ro)

    print(bar_idx)

    for b in range(n_per_group):
        bm = bars[b] # bar map
        plt.bar(bar_idx[b], bm['data'], width=bar_width, color=bm['color'], label=bm['name'])


    # Set the x-axis label
    if xaxis[0]['name'] != None:
        plt.xlabel(xaxis[0]['name'])

    # Set the y-axis label
    if yaxis[0]['name'] != None:
        plt.ylabel(yaxis[0]['name'])

    # Set the x-axis ticks
    try:
        xlabels = xaxis[0]['labels']
    except:
        xlabels = [xaxis[0]['format'].format(x) for x in xaxis[0]['data']]

    #plt.xticks([r + (bar_width+bar_pad)*((n_per_group+1)/2) for r in range(n_groups)], xlabels)
    xticklocs = np.sum(bar_idx, 0)
    xticklocs = np.divide(xticklocs, n_per_group)
    print(xticklocs)
    #xticklocs = [r + (bar_width+bar_pad)*((n_per_group+1)/2) for r in range(n_groups)]
    plt.xticks(xticklocs, xlabels)

    # Set the legend
    ax.legend(ncol=n_per_group, loc='upper center', columnspacing=1.0, handlelength=1.0 ,bbox_to_anchor=(0.5, 1.2))

    # Set the y-scale
    ax.set_yscale(yscale)

    plt.tight_layout(rect=(0,0,1,1.05))

    plt.savefig(out_file, bbox_inches='tight', pad_inches=0.05)

