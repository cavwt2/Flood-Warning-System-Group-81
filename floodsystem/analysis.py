from .datafetcher import fetch_measure_levels
import matplotlib
import numpy as np
def polyfit(dates,levels,p):
    """Returns a least squares polynomial fit for water level data"""
    x = matplotlib.dates.date2num(dates)
    d0 = x-x[0]
    p_coeff = np.polyfit(d0,levels,p)
    poly = np.poly1d(p_coeff)
    return(poly,d0)