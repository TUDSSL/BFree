import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import ScalarFormatter
from collections import namedtuple
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon
import csv

import plotstyle
import plotcolor

plotstyle.set_style()

fig = plt.figure()

gs1 = gridspec.GridSpec(nrows=2, ncols=1, wspace=0, hspace=0.5, right = 0.99, left = 0.101, bottom = 0.16, top = 0.98, width_ratios=[5], height_ratios=[1, 1])
ax2 = fig.add_subplot(gs1[0])
ax1= fig.add_subplot(gs1[1])


label_size = 8
ylim_1 = -1
ylim_2 = 35
hardware_delay = 0.0063
resistance = 47


time = []
voltage = []
with open("data/Modified-Power-Reset-Current.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV: 
        time.append(float(row[0]))
        voltage.append(float(row[1]))

time = [t/10000 for t in time]

# Divide by resistance 
current = [(v/resistance)*1000 for v in voltage]

# time = [0] + time
# current = [0] + current
ax1.plot(time, current, '-', lw = 1.5, color = 'green', markevery=5)

time_copy = time
oscilloscope_time = time[[n for n,i in enumerate(current) if i > 13  ][0]]

time = []
reset = []
with open("data/Modified-Power-Reset-Time.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV: 
        time.append(float(row[0]))
        reset.append(float(row[2]))


saleae_time = time[[n for n,i in enumerate(reset) if i == 1][0]]
sync_time = round(oscilloscope_time - saleae_time, 6)
time = [round((t + sync_time), 5) for t in time]
time.pop(0)

xlim_1 = time[0] - 0.1
xlim_2 = xlim_1 + 1.5


ax1.set_ylim([ylim_1, ylim_2])
ax1.set_xlim([xlim_1, xlim_2])

ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Current (mA)')
ax1.yaxis.set_label_coords(-0.08, 1.16)

ax1.set_title('BFree Boot Time')
ax1.set_xticks([xlim_1, xlim_1+0.25, xlim_1+0.5, xlim_1+0.75, xlim_1+1.0, xlim_1+1.25, xlim_1+1.5])
ax1.set_xticklabels(('0', '0.25', '0.5', '0.75', '1.0', '1.25', '1.5'))
# ax1.set_xticklabels(('0', '0.25', '0.5', '0.75', '1.0', '1.25', '1.5'))
# # plt.xticks(fontsize=label_size - 1, fontweight='bold')

ax1.tick_params(labelsize = label_size)


# ax1.grid(color='grey', linestyle=':', linewidth=1)


ax1.set_yticks([0, 15, 30])
ax1.set_yticklabels(('0', '15', '30'))


ax1.annotate('Power\n   ON', xy=(time[1] - 0.015, 6),
             xycoords='data',
             xytext=(time[1] - 0.1 , 20),
             textcoords='data',
             color = 'black',
             weight = 'bold',
             size = label_size - 1,
             arrowprops=dict(arrowstyle= '-|>',
                             color='black',
                             lw=1.5,
                             ls='-'),
             bbox=dict(pad= -1.5, facecolor="none", edgecolor="none")
           )


hardware_region = Polygon(((time[1] - hardware_delay,ylim_1), (time[1],ylim_1), (time[1], ylim_2), (time[1] - hardware_delay, ylim_2)),
                    color = plotcolor.DBLUE, alpha = 1, lw=0)

bootloader_region = Polygon(((time[1],ylim_1), (time[2],ylim_1), (time[2], ylim_2), (time[1], ylim_2)),
                    color = plotcolor.LBLUE, alpha = 1, lw=0)

port_init_region = Polygon(((time[2],ylim_1), (time[3],ylim_1), (time[3], ylim_2), (time[2], ylim_2)),
                    color = plotcolor.DGREEN, alpha = 1, lw=0)

safe_mode_region = Polygon(((time[3],ylim_1), (time[4],ylim_1), (time[4], ylim_2), (time[3], ylim_2)),
                    color = plotcolor.LGREEN, alpha = 1, lw=0)

file_system_region = Polygon(((time[4],ylim_1), (time[5],ylim_1), (time[5], ylim_2), (time[4], ylim_2)),
                    color = plotcolor.LORANGE, alpha = 1, lw=0)

# main_search_region = Polygon(((time[5],ylim_1), (time[6],ylim_1), (time[6], ylim_2), (time[5], ylim_2)),
#                     color = '#A53400', alpha = 1.0, lw=0)

# compilation_region = Polygon(((time[6],ylim_1), (time[7],ylim_1), (time[7], ylim_2), (time[6], ylim_2)),
#                     color = '#EDC9AF', alpha = 1, lw=0)

# before_execution_region = Polygon(((time[7],ylim_1), (time[8],ylim_1), (time[8], ylim_2), (time[7], ylim_2)),
#                     color = '#F48B09', alpha = 1, lw=0)

ax1.add_artist(hardware_region)
ax1.add_artist(bootloader_region)
ax1.add_artist(port_init_region)
ax1.add_artist(safe_mode_region)
ax1.add_artist(file_system_region)
# ax1.add_artist(main_search_region)
# ax1.add_artist(compilation_region)
# ax1.add_artist(before_execution_region)



############################################################################################################################################################

time = []
voltage = []
with open("data/Unmodified-Power-Reset-Current.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV: 
        time.append(float(row[0]))
        voltage.append(float(row[1]))

time = [t/10000 for t in time]

# Divide by resistance 
current = [(v/resistance)*1000 for v in voltage]

# time = [0] + time
# current = [0] + current
current_line = ax2.plot(time, current, '-', lw = 1.5, color = 'green', markevery=5, label='Current')

time_copy = time
oscilloscope_time = time[[n for n,i in enumerate(current) if i > 13  ][0]]

time = []
reset = []
with open("data/Unmodified-Power-Reset-Time.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV: 
        time.append(float(row[0]))
        reset.append(float(row[2]))


saleae_time = time[[n for n,i in enumerate(reset) if i == 1][0]]
sync_time = round(oscilloscope_time - saleae_time, 6)
time = [round((t + sync_time), 5) for t in time]
time.pop(0)

xlim_1 = time[0] - 0.1
xlim_2 = xlim_1 + 1.5


ax2.set_ylim([ylim_1, ylim_2])
ax2.set_xlim([xlim_1, xlim_2])

# ax2.set_xlabel('Time (s)', fontsize = label_size, fontweight='bold')
# ax2.set_ylabel('Current (mA)', fontsize = label_size)

ax2.set_title('CircuitPython Boot Time')
ax2.set_xticks([])
ax2.set_xticklabels(())
ax2.xaxis.set_ticks_position('none') 
# ax2.set_xticklabels([])
# ax2.set_xticklabels(('0', '0.25', '0.5', '0.75', '1.0', '1.25', '1.5'))
# # plt.xticks(fontsize=label_size - 1, fontweight='bold')

# ax2.set_xlabel('Time (s)', fontsize = label_size + 1)
# ax2.set_ylabel('Current (mA)', fontsize = label_size + 1)
# ax2.yaxis.set_label_coords(-0.08, 1.16)
ax2.tick_params(labelsize = label_size)

# ax2.grid(color='grey', linestyle=':', linewidth=1)


ax2.set_yticks([0, 15, 30])
ax2.set_yticklabels(('0', '15', '30'))
# ax2.xaxis.set_ticks_position('none') 

ax2.annotate('Power\n   ON', xy=(time[1] - 0.015, 6),
             xycoords='data',
             xytext=(time[1] - 0.1 , 20),
             textcoords='data',
             color = 'black',
             weight = 'bold',
             size = label_size - 1,
             arrowprops=dict(arrowstyle= '-|>',
                             color='black',
                             lw=1.5,
                             ls='-'),
             bbox=dict(pad= -1.5, facecolor="none", edgecolor="none")
           )


hardware_region = Polygon(((time[1] - hardware_delay,ylim_1), (time[1],ylim_1), (time[1], ylim_2), (time[1] - hardware_delay, ylim_2)),
                    color = plotcolor.DBLUE, alpha = 1, lw=0)

bootloader_region = Polygon(((time[1],ylim_1), (time[2],ylim_1), (time[2], ylim_2), (time[1], ylim_2)),
                    color = plotcolor.LBLUE, alpha = 1, lw=0)

port_init_region = Polygon(((time[2],ylim_1), (time[3],ylim_1), (time[3], ylim_2), (time[2], ylim_2)),
                    color = plotcolor.DGREEN, alpha = 1, lw=0)

safe_mode_region = Polygon(((time[3],ylim_1), (time[4],ylim_1), (time[4], ylim_2), (time[3], ylim_2)),
                    color = plotcolor.LGREEN, alpha = 1, lw=0)

file_system_region = Polygon(((time[4],ylim_1), (time[5],ylim_1), (time[5], ylim_2), (time[4], ylim_2)),
                    color = plotcolor.LORANGE, alpha = 1, lw=0)

# main_search_region = Polygon(((time[5],ylim_1), (time[6],ylim_1), (time[6], ylim_2), (time[5], ylim_2)),
#                     color = '#A53400', alpha = 1.0, lw=0)

# compilation_region = Polygon(((time[6],ylim_1), (time[7],ylim_1), (time[7], ylim_2), (time[6], ylim_2)),
#                     color = '#EDC9AF', alpha = 1, lw=0)

# before_execution_region = Polygon(((time[7],ylim_1), (time[8],ylim_1), (time[8], ylim_2), (time[7], ylim_2)),
#                     color = '#F48B09', alpha = 1, lw=0)

ax2.add_artist(hardware_region)
ax2.add_artist(bootloader_region)
ax2.add_artist(port_init_region)
ax2.add_artist(safe_mode_region)
ax2.add_artist(file_system_region)
# ax2.add_artist(main_search_region)
# ax2.add_artist(compilation_region)
# ax2.add_artist(before_execution_region)

legend_elements = [ current_line[0],
                    mpatches.Patch(color=plotcolor.DBLUE, label='Hardware', alpha = 1, linewidth = 0),
                    mpatches.Patch(color=plotcolor.LBLUE, label='Bootloader', alpha = 1, linewidth = 0),
                    mpatches.Patch(color=plotcolor.DGREEN, label='Port Init', alpha = 1, linewidth = 0),
                    mpatches.Patch(color=plotcolor.LGREEN, label='Safe Mode', alpha = 1, linewidth = 0),
                    mpatches.Patch(color=plotcolor.LORANGE, label='File System', alpha = 1, linewidth = 0)
                    # mpatches.Patch(color='#A53400', label='main() Search', alpha = 1.0, linewidth = 0),
                    # mpatches.Patch(color='#EDC9AF', label='Compilation', alpha = 1.0, linewidth = 0),
                    # mpatches.Patch(color='#F48B09', label='Before Execution', alpha = 1.0, linewidth = 0)
                    ]


ax1.legend(handles=legend_elements, loc = 'upper center', ncol = 3, bbox_to_anchor=(0.5, 3.7), handletextpad=0.15)


# ax.legend(loc = 'upper right', ncol = 1, bbox_to_anchor=(0.9, 1), prop={'weight':'bold', 'size':label_size - 1})

fig.set_size_inches(5, 1.5)
fig.savefig("cpy_time_overhead_modified.pdf", bbox_inches = 'tight', pad_inches=0.05)

#fig.tight_layout()
#plt.show()
