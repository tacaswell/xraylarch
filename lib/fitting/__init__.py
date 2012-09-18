#!/usr/bin/env python
from .parameter import Parameter, isParameter, param_value
from .minimizer import Minimizer, minimize, fit_report
from .confidence import conf_intervals , chisquare_map, conf_report

def confidence_report(conf_vals, **kws):
    """return a formatted report of confidence intervals calcualted
    by confidence_intervals"""
    
    return conf_report(conf_vals)

def confidence_intervals(minout, sigmas=(1, 2, 3),  **kws):
    """explicitly calculate the confidence intervals from a fit
    for supplied sigma values"""
    return conf_intervals(minout, sigmas=sigmas, **kws)

def chi2_map(minout, xname, yname, nx=11, ny=11,
             limits=None, **kws):
    """generate a confidence map for any two parameters for a fit

    Arguments
    ==========
       minout   output of minimize() fit (must be run first)
       xname    name of variable parameter for x-axis
       yname    name of variable parameter for y-axis
       nx       number of steps in x [11]
       ny       number of steps in y [11]
       xrange   range of calculations for x [x.best +/- 5*x.stderr]
       yrange   range of calculations for y [y.best +/- 5*y.stderr]

    Returns
    =======
        xpts, ypts, map
    """
    return chisquare_map(minout, xname, yname, nx=nx, ny=ny,
                         limits=limits, **kws)

def param(*args, **kws):
    "create a fitting Parameter as a Variable"
    if len(args) > 0 and isinstance(args[0], (str, unicode)):
        expr = args[0]
        args = args[1:]
        kws.update({'expr': expr})
    out = Parameter(*args, **kws)
    if 'name' not in kws:
        return out

def guess(value,  **kws):
    """create a fitting Parameter as a Variable.
    A minimum or maximum value for the variable value can be given:
       x = guess(10, min=0)
       y = guess(1.2, min=1, max=2)
    """
    kws.update({'vary':True})
    return param(value, **kws)

def is_param(obj, _larch=None, **kws):
    """return whether an object is a Parameter"""
    return isParameter(obj)
