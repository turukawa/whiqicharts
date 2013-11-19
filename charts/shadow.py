### PARAMETERS FOR MATPLOTLIB:
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.font_manager import FontProperties
from matplotlib import cm

wBlue = (06/255.0, 50/255.0, 92/255.0)
wGrey = (128/255.0,128/255.0,128/255.0)

def shadow_data():
    '''
    Sample data from IMF World Economic Outlook October 2013
    '''
    data = {"Title": "GDP at PPP 1980 - 2004", "X": "Gross domestic product at PPP", "Y": "Years",
            "Xdata": [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004],
            "Ydata": {"India": [295.93, 342.968, 376.872, 420.346, 451.903, 490.773, 524.542, 559.212, 634.572, 698.474, 764.36, 798.201, 861.138, 923.661, 1006.09, 1104.83, 1210.02, 1280.63, 1374.70, 1497.34, 1593.08, 1714.58, 1806.51, 1996.87, 2241.04],
                      "France": [541.678, 598.046, 650.507, 684.516, 719.405, 754.376, 786.949, 826.304, 895.156, 968.901, 1031.07, 1076.46, 1117.27, 1136.23, 1186.49, 1236.05, 1272.05, 1322.07, 1381.56, 1447.43, 1534.79, 1598.76, 1638.41, 1686.20, 1774.59],
                      "United Kingdom": [448.584, 484.296, 525.896, 567.612, 605.057, 648.569, 690.118, 744.21, 813.171, 866.705, 915.138, 933.372, 967.01, 1024.58, 1098.22, 1160.75, 1223.21, 1298.26, 1359.16, 1419.08, 1514.64, 1583.18, 1644.41, 1743.51, 1850.64],
                      "Italy": [513.79, 566.142, 605.287, 634.927, 678.672, 719.981, 755.505, 799.513, 862.217, 926.087, 980.058, 1027.21, 1059.39, 1075.36, 1121.87, 1178.34, 1213.46, 1257.26, 1289.30, 1326.70, 1406.42, 1465.42, 1494.66, 1523.83, 1582.85],
                      "Brazil": [449.72, 470.071, 502.211, 504.286, 549.899, 612.328, 671.803, 713.751, 740.695, 794.114, 789.165, 823.839, 838.685, 898.704, 966.794, 1030.56, 1071.94, 1127.08, 1139.71, 1158.93, 1236.30, 1281.22, 1335.49, 1377.81, 1494.69],
                      "Mexico": [352.499, 418.317, 441.955, 443.35, 474.722, 500.555, 494.754, 516.188, 541.026, 585.274, 638.269, 687.168, 727.919, 764.748, 817.845, 786.75, 846.414, 922.675, 976.807, 1017.15, 1093.19, 1113.77, 1132.39, 1171.58, 1256.22],
                      "Canada": [283.331, 320.635, 330.793, 353.196, 386.997, 418.469, 437.242, 467.469, 507.906, 541.473, 562.588, 569.149, 587.218, 615.254, 658.537, 690.689, 715.109, 758.283, 798.229, 850.091, 913.948, 950.662, 992.32, 1031.64, 1093.86],
                      "Spain": [274.691, 299.11, 321.604, 339.823, 357.86, 378.031, 398.888, 432.42, 471.213, 514.027, 553.548, 586.414, 604.884, 611.146, 638.726, 678.933, 708.064, 748.019, 789.924, 839.228, 901.666, 956.169, 997.15, 1048.49, 1110.97]}}
    return data

def lineShadow(*args, **kwargs):
    '''
    Line series with data in form:
        {"Title": "Title", "X": "X-axis", "Y": "Y-axis",
        "Xdata": [],
        "Ydata": {['series_name': [], for each series}}
    kwargs: line, if True then don't print shadow
            sline, the series to be highlighted
    '''
    fig = Figure(figsize=(9.5,3.5), dpi=100, facecolor='white')
    ax = plt.Axes(fig, [0.08, 0.1, 0.9, 0.6])
    fig.add_axes(ax)
    idxlen = len(kwargs["data"]["Ydata"])
    if "line" in kwargs and kwargs["line"] == True:
        for idx, series in enumerate(kwargs["data"]["Ydata"]):
            if "sline" in kwargs and kwargs["sline"] == series:
                clr = wBlue
            else:
                clr = cm.Spectral(float(idx+1)/idxlen)[:-1]
            ax.plot(kwargs["data"]["Ydata"][series], '-', ms=20, lw=2, color=clr, 
                        label=series)
    else:
        # Will throw an exception if "sline" has not been defined - and that's your fault
        slinedata = kwargs["data"]["Ydata"][kwargs["sline"]]
        del kwargs["data"]["Ydata"][kwargs["sline"]]
        # http://stackoverflow.com/a/4002806/295606
        shademax = map(max, zip(*kwargs["data"]["Ydata"].values()))
        shademin = map(min, zip(*kwargs["data"]["Ydata"].values()))
        ax.fill_between(np.arange(0, len(shademax)), shademin, shademax, 
                        alpha = 0.2, color=wGrey)
        ax.plot(slinedata, '-', ms=20, lw=2, color=wBlue, label=kwargs["sline"])
    ax.set_xlabel(kwargs["data"]['Y'], size='medium')
    ax.set_ylabel(kwargs["data"]['X'], size='medium')
    xNum = len(kwargs["data"]["Xdata"])
    ax.set_xlim(0,xNum-1)
    ax.set_xticks(range(0,xNum))
    ax.set_xticklabels(kwargs["data"]["Xdata"], fontsize=10, color='darkgrey')
    ax.set_yticklabels(ax.get_yticks(),fontsize=10, color='darkgrey')
    # Set up the legend
    # bbox_to_anchor, a tuple of 4 floats (x, y, width, height of the bbox), 
    # or a tuple of 2 floats (x, y with width=height=0).
    # http://matplotlib.sourceforge.net/users/legend_guide.html
    box = ax.get_position()
    # this moves the chart
    ax.set_position([box.x0, box.y0 + box.height * 0.3,box.width, 
                     box.height * 1.1])
    fontP = FontProperties()
    fontP.set_size('xx-small')
    # this places the legend
    lgnd = ax.legend(loc='upper center', bbox_to_anchor=(0.02, -0.32, 0.94, 0.1), 
                     ncol=3, mode='expand', borderaxespad=0. , prop = fontP)
    lgnd.draw_frame(False)
    # http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg12449.html
    # update the font size of the x and y axes
    # https://www.cfa.harvard.edu/~jbattat/computer/python/pylab/
    fontsize=9
    for tick in ax.xaxis.get_major_ticks():
      tick.label1.set_fontsize(fontsize)
    for tick in ax.yaxis.get_major_ticks():
      tick.label1.set_fontsize(fontsize)
    ax.set_xticklabels([i.get_text() for i in ax.xaxis.get_majorticklabels()], 
                       rotation=30)
    # Return the plot
    FigureCanvasAgg(fig).print_figure('shadow')
    '''
    # Return the Django plot
    canvas = FigureCanvasAgg(fig)
    response = HttpResponse(mimetype='image/png')
    canvas.print_png(response)   
    return response
    '''