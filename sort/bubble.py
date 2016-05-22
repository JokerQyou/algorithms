#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from docopt import docopt

from _base import SortBase, is_sorted

__doc__ = '''
bubble sort.

Usage:
    bubble.py <n>...
'''


class Bubble(SortBase):
    """冒泡排序"""

    @staticmethod
    def sort(l):
        for n in xrange(len(l) - 1, 0, -1):
            for i in xrange(n):
                if l[i] > l[i + 1]:
                    l[i], l[i + 1] = l[i + 1], l[i]


if __name__ == '__main__':
    args = docopt(__doc__)
    l = [int(i) for i in args['<n>']]
    Bubble.sort(l)
    print('Result: {}\nSorted: {}'.format(l, is_sorted(l)))
