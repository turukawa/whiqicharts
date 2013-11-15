### PARAMETERS FOR MATPLOTLIB:
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from pylab import array
from decimal import Decimal
from matplotlib.font_manager import FontProperties
from matplotlib import cm
from matplotlib.lines import Line2D

def comet_data():
    '''
    Produce five random data series for use as sample chart.
    Data is presented as an array of (x, y, z)
    '''
    data = {"Title": "Title", "X": "X-axis", "Y": "Y-axis", "Z": "Z-axis",
            "Data": {"Item1": [[4.3,7.4,0.2],[4.7,7.3,0.3],[4.8,7.1,0.4],[5.3,6.5,0.5],[5.7,6.3,0.6]],
                     "Item2": [[2.1,3.4,0.2],[1.9,3.7,0.3],[1.8,3.8,0.4],[1.4,4.3,0.5],[1.2,4.5,0.6]],
                     "Item3": [[6.5,4.5,0.1],[6.7,4.3,0.2],[6.9,4.1,0.3],[7.2,3.9,0.4],[7.5,3.6,0.5]],
                     "Item4": [[5.5,4.4,0.1],[5.3,4.6,0.2],[5,4.9,0.3],[4.8,5.1,0.4],[4.6,5.3,0.5]]}}
    return data

def comet(data):
    '''
    Data point is (x, y, z)
    Data structure is: 
        {"Title": "Title", "X-": "X-axis", "Y": "Y-axis", "Z": "Z-axis",
        "Data": ['series_name': [x,y,z],[x,y,z], etc. for each series]}
    Each new series will get its own colour assigned;
    '''
    fig = Figure(figsize=(7,7), dpi=100, facecolor='white')
    # axes(rect, axisbg='w') where rect = [left, bottom, width, height] in 
    # normalized (0, 1) units
    # http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.axes
    ax = plt.Axes(fig, [0.08, 0.06, 0.9, 0.9])
    fig.add_axes(ax)
    idxlen = len(data['Data'])
    plt_list = [] # list for holding all the points plotted
    entity_list = []
    for idx, series in enumerate(data['Data']):
        clr = cm.Spectral(float(idx+1)/idxlen)[:-1]
        srslen = len(series)
        for a, [x, y, z] in enumerate(data['Data'][series]):
            try:
                # http://stackoverflow.com/q/10422504
                p, = ax.plot(x, y, marker='o', ms=100*z, mec=None, mew=0.0, 
                            alpha=(a+1)/float(srslen), mfc=clr)
                if a+1 == srslen:
                    ax.text(x, y, series, fontsize=8)
            except:
                p = None
        if p:
            plt_list.append(p)
            entity_list.append(series)
    # http://matplotlib.sourceforge.net/api/axes_api.html#matplotlib.axes.Axes.set_xlabel
    ax.set_xlabel(data['X'], size='medium')
    ax.set_ylabel(data['Y'], size='medium')
    # Set up the legend
    # http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.Figure
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.2,box.width, 
                     box.height * 0.8])
    fontP = FontProperties()
    fontP.set_size('x-small')
    lgnd = ax.legend(plt_list, entity_list, loc='upper center', 
                     bbox_to_anchor=(0.5, -0.1), ncol=5, numpoints=1, 
                     markerscale=0.5, prop=fontP)
    # http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg12449.html
    lgnd.draw_frame(False)
    # Create the grid
    # http://matplotlib.sourceforge.net/api/artist_api.html#matplotlib.lines.Line2D
    # http://matplotlib.sourceforge.net/users/artists.html#axis-containers
    xax = ax.xaxis.get_ticklocs()
    yax = ax.yaxis.get_ticklocs()
    fxax = xax[-1] - xax[0]
    fyax = yax[-1] - yax[0]
    try:
        topx = 1 - (xax[-1] - min(xax[-1], yax[-1]))/fxax
    except:
        topx = 1.
    try:
        topy = 1 - (yax[-1] - min(xax[-1], yax[-1]))/fyax
    except:
        topy = 1.
    try:
        botx = (yax[0] - min(xax[0], yax[0]))/fxax
    except:
        botx = 0.
    try:
        boty = (xax[0] - min(xax[0], yax[0]))/fyax
    except:
        boty = 0.
    # update the font size of the x and y axes
    # https://www.cfa.harvard.edu/~jbattat/computer/python/pylab/
    fontsize=10
    for tick in ax.xaxis.get_major_ticks():
      tick.label1.set_fontsize(fontsize)
    for tick in ax.yaxis.get_major_ticks():
      tick.label1.set_fontsize(fontsize)
    # Return the plot
    FigureCanvasAgg(fig).print_figure('Test')