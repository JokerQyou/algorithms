#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from docopt import docopt

from ._base import SortBase, is_sorted

__doc__ = '''
selection sort.
Usage:
    selection.py <n>...
'''


class Selection(SortBase):
    """选择排序"""

    @staticmethod
    def sort(l):
        N = len(l)
        # Start from the 1st element
        for x in xrange(0, N):
            min_ = x
            # Find the smallest number from the remaining ones,
            # and exchange it with the first of all unsorted ones
            for y in xrange(x + 1, N):
                if l[y] < l[min_]:
                    min_ = y
			# enchange elements
            l[x], l[min_] = l[min_], l[x]


if __name__ == '__main__':
    args = docopt(__doc__)
    l = [int(i) for i in args['<n>']]
    Selection.sort(l)
    print('Result: {}\nSorted: {}'.format(l, is_sorted(l)))
