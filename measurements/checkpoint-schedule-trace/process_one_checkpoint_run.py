import argparse
import sys
import csv
import os

import statistics as stat
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import ticker

import plotcolor
import plotstyle

import parse_trace as pt

parser = argparse.ArgumentParser(description='Generate small checkpoint plot')
parser.add_argument("data", help=".csv file containing the data")
parser.add_argument("-o", "--outfile", help="Output file (default: <csv_name.pdf>")
parser.add_argument("-l", "--outlegend", help="Output legend file (default: None")

args = parser.parse_args()
content_file = args.data
out_file = args.outfile
out_legend = args.outlegend

data_file = content_file
print('Data file:', data_file)
print('Output file', out_file)
print('Output legend file', out_legend)

pt.process(data_file)

plotstyle.set_style()

figsize = (4, 1.5)
fig, ax = plt.subplots(figsize = figsize)

ax.xaxis.grid(False)
ax.yaxis.grid(False)

for pfll in pt.pfail_fitted_low_list:
    rx = pfll[0]
    rxd = pfll[1]-rx
    rect_pfail_low = patches.Rectangle((rx,0), rxd , 1.05, facecolor=plotcolor.DBLUE, alpha=1)
    ax.add_patch(rect_pfail_low)

for pfhl in pt.lowpass_list(pt.pfail_high_list, 0.01):
    rx = pfhl[0]
    rxd = pfhl[1]-rx
    rect_pfail_high = patches.Rectangle((rx,0), rxd , 1.05, facecolor=plotcolor.LBLUE, alpha=1)
    ax.add_patch(rect_pfail_high)

for resthl in pt.restore_high_list:
    rx = resthl[0]
    rxd = resthl[1]-rx
    rect_restore = patches.Rectangle((rx,0), rxd , 1, facecolor=plotcolor.DGREEN, linewidth=0.5, edgecolor='black', alpha=1)
    ax.add_patch(rect_restore)

for cphl in pt.checkpoint_fitted_high_list:
    rx = cphl[0]
    rxd = cphl[1]-rx
    rect_checkpoint = patches.Rectangle((rx,0), rxd , 1, facecolor=plotcolor.LGREEN, linewidth=0.5, edgecolor='black', alpha=1)
    ax.add_patch(rect_checkpoint)

print(pt.pd_active_step_time)
print(pt.pd_active_step)
act_step_time = pt.pd_active_step_time
act_step = pt.pd_active_step

act_step_time.insert(0, 0.0)
act_step.insert(0, 0.0)

act_step_time.append(act_step_time[-1]+5)
act_step.append(0.0)
act_step = [x*1.05 for x in act_step]

ax.plot(act_step_time, act_step, linewidth=1, color='black', drawstyle='steps-post', zorder=200)

print('Plotting data')

# X labels
ax.set_xlabel('Time (s)')

ax.tick_params(axis='y', which='minor', left=False)

#x_start=pt.pd_vcap_time[0]+0.75
print(pt.pd_vcap_time[0])
print(pt.pd_active_step_time)
x_start=pt.pd_active_step_time[1]-0.2
x_end=x_start+2
ax.set_xlim(x_start, x_end)

xticks = [0, 0.5, 1, 1.5, 2, 2.5, 3]
real_xticks = [x+x_start for x in xticks]
labels_xticks=['${:.1f}$'.format(x) for x in xticks]

ax.xaxis.set_major_locator(ticker.FixedLocator(real_xticks))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(labels_xticks))

## Y labels
ax.set_ylim(0, 1.1)
#desired_yticks_labels=['\\textbf{Off}', '\\textbf{On}']
desired_yticks_labels=['Off', 'On']
desired_yticks=[0, 1.05]
ax.yaxis.set_major_locator(ticker.FixedLocator(desired_yticks))
ax.yaxis.set_major_formatter(ticker.FixedFormatter(desired_yticks_labels))

fig.tight_layout()
fig.savefig(out_file, bbox_inches='tight', pad_inches=0.05)

if out_legend != None:
    # Legend figure
    figlegend = plt.figure(figsize=(3,0.5))
    figlegend.legend([rect_pfail_high, rect_pfail_low, rect_restore, rect_checkpoint],
            ['Normal operation', 'Low energy operation', 'Restore', 'Checkpoint'],
            loc='center',
            ncol=2,
            )
    figlegend.tight_layout()
    figlegend.savefig(out_legend)
