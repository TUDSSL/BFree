import matplotlib.pyplot as plt
import numpy as np

import plotcolor
import plotstyle

# Template source https://matplotlib.org/3.1.3/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html

category_names_1 = ['Never heard of it', 'Heard of it', 'I have used in once', 'I have used more than once']

results_1 = {
    'CircuitPython': [6, 3, 0, 0],
    'Python': [0, 0, 0, 9],
    'Adafruit Metro M0': [6, 3, 0, 0],
    'Arduino Uno': [0, 3, 1, 5]
}

category_names_2 = ['No experience', 'Some experience', 'A lot of experience', 'Expert'] # check 'Very little experience'?

results_2 = {
    'Circuits design': [5, 2, 1, 1],
    'Programming': [0, 1, 6, 2]
}

category_names_3 = ['Strongly disagree', 'Disagree', 'Neither agree nor disagree', 'Agree', 'Strongly agree']

results_3 = {
    'Battery-free embedded MCUs programming\neasier with Python than C/C++': [0, 0, 1, 5, 3],
    'BFree with Metro M0 board helps develop\nbattery-free apps': [0, 0, 1, 5, 3],
    'Easy to develop battery-less apps using\nPython with BFree': [0, 0, 2, 4, 3],
    'Battery-less temperature application\nas valuable': [0, 1, 0, 6, 2],
    'Batteries used by embedded MCUs are\nthreat to the environment': [0, 1, 2, 5, 1],
    'Makers/hobbyists interested in building\nbattery-free systems': [0, 0, 0, 6, 3]
}

category_names_4 = ['Very unlikely', 'Unlikely', 'Neutral', 'Likely', 'Very likely']

results_4 = {
    'System handling program correctness\ndespite power failures would help': [5, 20, 37, 188, 107],
    'System handling program correctness\ndespite power failures would save time': [17, 37, 56, 122, 125],
    'Rewriting (Python) code to be correct\ndespite power failures is time-consuming': [6, 25, 53, 144, 129]
}

category_names_5 = ['No experience', 'Very little experience', 'Some experience', 'A lot of experience', 'Expert']

results_5 = {
    'Any programming language': [26, 85, 170, 70, 5],
    'Python language programming': [120, 97, 107, 27, 5],
    'C/C++ programming': [159, 64, 85, 43, 5]
}

category_names_6 = ['Never heard of it', 'Heard of it', 'I have used in once', 'I have used more than once']

results_6 = {
    'Adafruit Metro M0 or Arduino Uno': [97, 127, 61, 71],
    'CircuitPython': [291, 61, 3, 1]
}

#Do you think that Python makes programming battery-free embedded micro-controllers easier than using C/C++ programming language?
#Do you think that BFree with Metro M0 board would help you develop battery-free applications?
#Was it easy to develop battery-less application using Python with BFree shield?
#Do you perceive the battery-less temperature application as valuable (as in: perpetual operation, no environmental impact)?
#Do you think that batteries used by embedded micro-controllers are a threat to the environment?
#Do you think that makers and hobbyists would be interested in building battery-free systems?


def survey(ax, results, category_names):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    #category_colors = plt.get_cmap('RdYlGn')(np.linspace(0.15, 0.85, data.shape[1]))
    category_colors = [plotcolor.DRED, plotcolor.LORANGE, plotcolor.YELLOW, plotcolor.LGREEN, plotcolor.DGREEN]

    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    data_max = np.sum(data, axis=1).max()
    ax.set_xlim(0, data_max)

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,label=colname, color=color)
        xcenters = starts + widths / 2

        for y, (x, c) in enumerate(zip(xcenters, widths)):
            fontsize = 8
            #if c < data_max*0.04:
            if c <= 0:
                marker = str()
            else:
                if c < data_max*.02:
                    fontsize=6
                marker = '\\textbf{' + str(int(c)) + '}'
            #ax.text(x, y, marker, ha='center', va='center', color=text_color, fontsize=6)
            ax.text(x, y, marker, ha='center', va='center', fontsize=fontsize)

    ax.legend(ncol=len(category_names), bbox_to_anchor=(1, 1), loc='lower right', fontsize=8)

    labels = ax.get_yticklabels()
    plt.setp(labels, fontsize=8)

    #return fig, ax

# Set the plot style to use LaTex
plotstyle.set_style()
plt.rcParams.update({'ytick.minor.visible': False})

fig_1, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [2, 1]}, figsize=(7, 2.3), tight_layout=True)

survey(ax0, results_1, category_names_1)
survey(ax1, results_2, category_names_2)

fig_2, ax2 = plt.subplots(figsize=(7, 2.8), tight_layout=True)

survey(ax2, results_3, category_names_3)

fig_3, ax3 = plt.subplots(figsize=(7, 1.5), tight_layout=True)

survey(ax3, results_4, category_names_4)

fig_4, (ax4, ax5) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [2, 1]}, figsize=(7, 2), tight_layout=True)

lab = ax4.get_yticklabels()

survey(ax4, results_5, category_names_5)
survey(ax5, results_6, category_names_6)

#plt.show()

# Save the figures

plt.tight_layout(rect=(0,0,1,1.03)) # Remove some headroom after placing the legend above

fig_1.savefig('user-experience-study-questions.pdf', bbox_inches='tight', pad_inches=0.05)
fig_2.savefig('user-experience-study-results.pdf', bbox_inches='tight', pad_inches=0.05)
fig_3.savefig('language-comparative-study-results.pdf', bbox_inches='tight', pad_inches=0.05)
fig_4.savefig('language-comparative-study-questions.pdf', bbox_inches='tight', pad_inches=0.05)
