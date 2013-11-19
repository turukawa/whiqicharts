### PARAMETERS FOR MATPLOTLIB:
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.font_manager import FontProperties
from matplotlib import cm

def comet_data():
    '''
    Produce five random data series for use as sample chart.
    Data is presented as an array of (x, y, z)
    Sample data from IMF World Economic Outlook October 2013, annual data from 2013 to 2018
    '''
    data = {"Title": "Economic Variance", "X": "Gross domestic product based on PPP per capita", "Y": "Inflation, average consumer prices", "Z": "Unemployment rate",
            "Data": {"Brazil": [[12117.752,6.346,5.8],[12528.232,5.771,6],[13090.807,5.309,6.5],[13719.01,4.698,6.5],[14396.012,4.5,6.5],[15105.358,4.5,6.5]],
                     "Indonesia": [[5181.563,7.257,5.9],[5477.907,7.542,5.8],[5842.114,5.753,5.5],[6232.261,5.236,5.3],[6647.787,4.729,5.2],[7090.518,4.505,5.2]],
                     "China": [[9828.32,2.735,4.1],[10660.889,2.971,4.1],[11586.633,3,4.1],[12594.169,3,4.1],[13681.981,3,4.1],[14861.484,3,4.1]],
                     "Mongolia": [[5932.083,9.671,6.1],[6633.784,7.482,5.4],[7059.292,7.311,4.6],[7352.114,6.533,4.3],[8099.178,6.141,4.1],[8651.493,5.912,3]],
                     "Mauritius": [[16082.193,4.742,8.262],[16966.211,4.731,8.034],[18025.106,5.058,7.521],[19162.869,5.012,7.395],[20358.783,5.012,7.423],[21627.805,5.012,7.423]]}}
    return data

def comet(data):
    '''
    Data point is (x, y, z)
    Data structure is: 
        {"Title": "Title", "X": "X-axis", "Y": "Y-axis", "Z": "Z-axis",
        "Data": ['series_name': [x,y,z],[x,y,z], etc. for each series]}
    Each new series will get its own colour assigned;
    '''
    fig = Figure(figsize=(7,7), dpi=100, facecolor='white')
    # axes(rect, axisbg='w') where rect = [left, bottom, width, height] in 
    # normalized (0, 1) units
    # http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.axes
    ax = plt.Axes(fig, [0.08, 0.06, 0.9, 0.9])
    fig.add_axes(ax)
    # Get some constants
    idxlen = len(data['Data'])
    Zmax = []
    for m in data['Data'].values():
        Zmax.append(max([z for [x,y,z] in m]))
    Zmax = max(Zmax)*1.8
    plt_list = [] # list for holding all the points plotted
    entity_list = []
    for idx, series in enumerate(data['Data']):
        clr = cm.Spectral(float(idx+1)/idxlen)[:-1]
        srslen = len(data['Data'][series])
        for a, [x, y, z] in enumerate(data['Data'][series]):
            try:
                # http://stackoverflow.com/q/10422504
                p, = ax.plot(x, y, marker='o', ms=100*z/Zmax, mec=None, mew=0.0, 
                            alpha=(a+1)/float(srslen), mfc=clr)
                if a+2 == srslen:
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
    # Create the grid (centre-line grid to create quadrants)
    # http://matplotlib.sourceforge.net/api/artist_api.html#matplotlib.lines.Line2D
    # http://matplotlib.sourceforge.net/users/artists.html#axis-containers
    # http://matplotlib.org/examples/pylab_examples/axhspan_demo.html
    xax = ax.xaxis.get_ticklocs()
    yax = ax.yaxis.get_ticklocs()
    fxax = (max(xax)-min(xax))/2 + min(xax) # Find the midpoint
    fyax = (max(yax)-min(yax))/2 + min(yax)
    ax.axhline(y=fyax, linewidth=1, color='black')
    ax.axvline(x=fxax, linewidth=1, color='black')
    # update the font size of the x and y axes
    # https://www.cfa.harvard.edu/~jbattat/computer/python/pylab/
    fontsize=10
    for tick in ax.xaxis.get_major_ticks():
      tick.label1.set_fontsize(fontsize)
    for tick in ax.yaxis.get_major_ticks():
      tick.label1.set_fontsize(fontsize)
    # Return the plot
    FigureCanvasAgg(fig).print_figure('comet')