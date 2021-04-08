import matplotlib.pyplot as plt

#import matplotlib.ticker
#class MyLocator(matplotlib.ticker.AutoMinorLocator):
#    def __init__(self, n=2):
#        super().__init__(n=n)
#matplotlib.ticker.AutoMinorLocator = MyLocator

def set_style():
    # Plotting
    plt.style.use('seaborn-whitegrid')
    #print(plt.rcParams)
    #plt.style.use('seaborn-ticks')
    new_rc_params_style = {
            'xtick.major.size': 4,
            'xtick.minor.size': 2,
            'xtick.minor.width': 0.6,
            'xtick.minor.visible': True,

            'ytick.major.size': 4,
            'ytick.minor.size': 2,
            'ytick.minor.width': 0.6,
            'ytick.minor.visible': True,
            'axes.edgecolor': "0.5",

            }
    plt.rcParams.update(new_rc_params_style)

    new_rc_params = {
            'text.usetex': True,
             #'svg.fonttype': 'none',
             'text.latex.preamble': r'\usepackage{libertine}',
             'font.size': 8,
             'font.family': 'sans-serif',
             'font.serif' : 'libertine',
             'mathtext.fontset': 'custom',
             'mathtext.rm': 'libertine',
             'mathtext.it': 'libertine:italic',
             'mathtext.bf': 'libertine:bold'
             }
    plt.rcParams.update(new_rc_params)
