# -*- coding: utf-8 -*-

"""Copyright 2015 Roger R Labbe Jr.


Code supporting the book

Kalman and Bayesian Filters in Python
https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python


This is licensed under an MIT license. See the LICENSE.txt file
for more information.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from IPython.core.display import HTML
import json
import matplotlib
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
import os.path
import sys
import warnings

# version 1.4.3 of matplotlib has a bug that makes
# it issue a spurious warning on every plot that
# clutters the notebook output
if matplotlib.__version__ == '1.4.3':
    warnings.simplefilter(action="ignore", category=FutureWarning)

try:
    matplotlib.style.use('default')
except:
    pass

pylab.rcParams['figure.max_open_warning'] = 50

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv


def set_style():
    version = [int(version_no) for version_no in matplotlib.__version__.split('.')]

    try:
        if sys.version_info[0] >= 3:
            style = json.load(open("./style.json"))
        else:
            style = json.load(open("./style.json"), object_hook = _decode_dict)
        plt.rcParams.update(style)
        print('update plt style')
    except:
        pass
		
    np.set_printoptions(suppress = True, precision = 3, 
                        threshold = 10000.0, linewidth = 70,
                        formatter = {'float': lambda x: ' {:.3}'.format(x)})

    np.set_printoptions(suppress = True)

    style = '''
        <style>
        .output_wrapper, .output {
            height:auto !important;
            max-height:100000px; 
        }
        .output_scroll {
            box-shadow:none !important;
            webkit-box-shadow:none !important;
        }
        </style>
    '''
    return HTML(style)
