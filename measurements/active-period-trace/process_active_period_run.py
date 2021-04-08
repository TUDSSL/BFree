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

parser = argparse.ArgumentParser(description='Generate large on-time plot')
parser.add_argument("data", help=".csv file containing the data")
parser.add_argument("-o", "--outfile", help="Output file (default: <csv_name.pdf>")

args = parser.parse_args()
content_file = args.data
out_file = args.outfile

data_file = content_file
print('Data file:', data_file)
print('Output file', out_file)

pt.process(data_file)

plotstyle.set_style()

figsize = (7, 2)
fig, ax_v = plt.subplots(figsize = figsize)
ax = ax_v.twinx()

ax.xaxis.grid(False)
ax.yaxis.grid(False)

ax_v.yaxis.grid(False)
ax_v.xaxis.grid(False)

line_cap_voltage = ax_v.plot(pt.pd_vcap_time, pt.pd_vcap_voltage, color=plotcolor.DGREEN, linewidth=2)

for pfll in pt.pfail_fitted_low_list:
    rx = pfll[0]
    rxd = pfll[1]-rx
    rect_pfail_low = patches.Rectangle((rx,0), rxd , 1, facecolor=plotcolor.DBLUE, alpha=1)
    ax.add_patch(rect_pfail_low)

for pfhl in pt.lowpass_list(pt.pfail_high_list, 0.01):
    rx = pfhl[0]
    rxd = pfhl[1]-rx
    rect_pfail_high = patches.Rectangle((rx,0), rxd , 1, facecolor=plotcolor.LBLUE, alpha=1)
    ax.add_patch(rect_pfail_high)

for pfhl in pt.active_high_list:
    rx = pfhl[0]
    rxd = pfhl[1]-rx
    rect_active_high = patches.Rectangle((rx,1), rxd , 1.2, facecolor=plotcolor.LGREEN, alpha=0.4)
    ax.add_patch(rect_active_high)

ax.plot(pt.pd_active_step_time, pt.pd_active_step, linewidth=1, color='black', drawstyle='steps-post', zorder=200)

print('Plotting data')

# X labels
x_start=pt.pd_vcap_time[0]+4
x_end=x_start+80
ax.set_xlim(x_start, x_end)

xticks = range(0, 90, 10)
real_xticks = [x+x_start for x in xticks]
labels_xticks=['${:.0f}$'.format(x) for x in xticks]
plt.xticks(real_xticks, labels_xticks)

# Y labels
desired_yticks_labels=['\\textbf{Off}', '\\textbf{On}']
desired_yticks=[0, 1]
ax.yaxis.set_major_locator(ticker.FixedLocator(desired_yticks))
ax.yaxis.set_major_formatter(ticker.FixedFormatter(desired_yticks_labels))

ax_v.set_ylim(1.5, 4)
ax_v.set_ylabel('Capacitor voltage (V)')

ax.set_ylim(0, 2)
ax.tick_params(axis='y', which='minor', right=False)

ax_v.set_xlabel('Time (s)')

# Set the legend
#ax.legend(ncol=n_per_group, loc='upper center', bbox_to_anchor=(0.5, 1.2))
ax.legend([line_cap_voltage[0], rect_active_high, rect_pfail_high, rect_pfail_low],
        ['Capacitor voltage', 'Active', 'Normal operation', 'Low energy operation'],
        loc='upper center',
        ncol=4,
        bbox_to_anchor=(0.5, 1.2)
        )


# Set the plot order
ax_v.set_zorder(1)
ax_v.patch.set_visible(False)  # prevents ax1 from hiding ax2

#plt.tight_layout()
plt.tight_layout(rect=(0,0,1,1.03)) # Remove some headroom after placing the legend above

plt.savefig(out_file, bbox_inches='tight', pad_inches=0.05)

