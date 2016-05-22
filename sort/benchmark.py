#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import copy
import time

from docopt import docopt
from terminaltables import AsciiTable
import numpy

from _base import is_sorted
from insertion import Insertion
from selection import Selection
from shell import Shell
from bubble import Bubble

__doc__ = '''
benchmark.py

Usage:
    benchmark.py <length> <repeat>
'''


def run(func, length, repeat):
    '''
    Run a sort algorithm for {repeat} times
    on a random sequence with {length} floats.
    '''
    total = 0.0
    count = repeat
    while count > 0:
        l = numpy.random.uniform(low=0.0, high=1.0, size=length)
        ts = time.time()
        func(l)
        te = time.time()
        # If an algorithm does not sort the sequence right, it's worth nothing
        assert is_sorted(l)
        total += te - ts
        count -= 1
    return total, 'float', False


def run_ordered(func, length, repeat):
    '''
    Run a sort algorithm for {repeat} times
    on an ordered (sorted) sequence with {length} floats.
    '''
    total = 0.0
    count = repeat
    while count > 0:
        l = [i for i in xrange(length)]
        ts = time.time()
        func(l)
        te = time.time()
        assert is_sorted(l)
        total += te - ts
        count -= 1
    return total, 'int', True


def sort_compare(length, repeat):
    '''Compare sort algorithms'''

    # This controls what algorithms will be compared
    algorithms = {
        'bubble': Bubble.sort,
        'selection': Selection.sort,
        'insertion': Insertion.sort,
        'insertion_1st_version': Insertion.sort_1st_version,
        'insertion_2nd_version': Insertion.sort_2nd_version,
        'shell': Shell.sort,
    }
    run_funcs = (run, run_ordered, )
    # 1st row is the table header
    table_data = [
        ['Algorithm', 'total time', 'list length', 'repeat', 'item type', 'already sorted', ],
    ]

    for func in run_funcs:
        data = copy.deepcopy(table_data)
        for alg in algorithms.keys():
            alg_func = algorithms[alg]
            time_total, type_, pre_ordered = func(alg_func, length, repeat)
            data.append([
                alg, '{:.3f}'.format(time_total),
                str(length), str(repeat), str(type_), str(pre_ordered),
            ])
        print(AsciiTable(data).table)


if __name__ == '__main__':
    args = docopt(__doc__)
    sort_compare(
        int(args['<length>']), int(args['<repeat>'])
    )
