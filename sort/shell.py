#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from docopt import docopt

from ._base import SortBase, is_sorted

__doc__ = '''
shell sort.

Usage:
    shell.py <n>...
'''


class Shell(SortBase):
    """希尔排序"""

    @staticmethod
    def sort(l):
        N = len(l)
        h = 1
        N_ = N / 3
        while h < N_:
            h = 3 * h + 1
        while h >= 1:
            for i in xrange(h, N):
                j = i
                while j >= h and l[j] < l[j - h]:
                    l[j], l[j - h] = l[j - h], l[j]
                    j -= h
            h = h / 3


if __name__ == '__main__':
    args = docopt(__doc__)
    l = [int(i) for i in args['<n>']]
    Shell.sort(l)
    print('Result: {}\nSorted: {}'.format(l, is_sorted(l)))
