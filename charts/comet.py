### PARAMETERS FOR MATPLOTLIB:
import matplotlib as mpl
import matplotlib.pyplot as plt

def comet_data():
    '''
    Produce five random data series for use as sample chart.
    Data is presented as an array of (x, y, z)
    '''
    data = []
    return data

def comet(data):
    '''
    Data point is (x, y, z)
    Data structure is: 
        {"Title": "Title", "X-": "X-axis", "Y": "Y-axis", "Z": "Z-axis",
        "Data": [[[x,y,z],[x,y,z], etc. for each series]}
    Each new series will get its own colour assigned;
    '''
    fig = Figure(figsize=(7,7), dpi=100, facecolor='white')
    #fig.subplots_adjust(bottom=0.4, top=0.98)
    #ax = fig.add_subplot(111)
    # axes(rect, axisbg='w') where rect = [left, bottom, width, height] in normalized (0, 1) units
    # http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.axes
    ax = plt.Axes(fig, [0.08, 0.06, 0.9, 0.9])
    fig.add_axes(ax)
    cllen = len(data['Data'])
    plt_list = [] # list for holding all the points plotted
    entity_list = []
    for cl in range()
        clr = cm.spectral(float(cl)/cllen)[:-1]
        for a, d in enumerate(series_dict['Years']):
            try:
                p = ax.plot(x, y, marker='o', ms=100*z, mec=None, mew=0.0, alpha=(a+1)/float(yrlen), mfc=clr)
                if (a+1)/float(yrlen)==1.0:
                    ax.text(x, y, e.name, fontsize=8)
            except:
                p = None
        if p:
            plt_list.append(p)
            entity_list.append(e.name)
    # http://matplotlib.sourceforge.net/api/axes_api.html#matplotlib.axes.Axes.set_xlabel
    ax.set_xlabel(data['X'], size='large')
    ax.set_ylabel(data['Y'], size='large')
    # ax.set_yscale('log')
    # ax.set_xscale('log')
    # Set up the legend
    # http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.Figure
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.2,box.width, box.height * 0.8])
    fontP = FontProperties()
    fontP.set_size('x-small')
    lgnd = ax.legend(plt_list, entity_list, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5, numpoints=1, markerscale=0.5, prop=fontP)
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
    #ax.add_line(Line2D([0.5, 0.5], [0, 1], transform=ax.transAxes,linewidth=1,color='black'))
    ax.add_line(Line2D([botx, topx], [boty, topy], transform=ax.transAxes,linewidth=1,color='black'))
    # update the font size of the x and y axes
    # https://www.cfa.harvard.edu/~jbattat/computer/python/pylab/
    fontsize=10
    for tick in ax.xaxis.get_major_ticks():
      tick.label1.set_fontsize(fontsize)
    for tick in ax.yaxis.get_major_ticks():
      tick.label1.set_fontsize(fontsize)
    # Return the plot
    canvas = FigureCanvasAgg(fig)
    response = HttpResponse(mimetype='image/png')
    canvas.print_png(response)    
    return response