#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from docopt import docopt

from ._base import SortBase, is_sorted

__doc__ = '''
insertion sort.
Usage:
    insertion.py <n>...
'''


class Insertion(SortBase):
    """插入排序"""

    @staticmethod
    def sort_1st_version(l):
        '''
        The original insertion sort taught by 'Algorithms'
        and http://visualgo.net/sorting.
        It moves elements one by one, which is slow.
        '''
        for i in xrange(1, len(l)):
            j = i
            while j > 0:
                if l[j] < l[j - 1]:
                    l[j], l[j - 1] = l[j - 1], l[j]
                j -= 1

    @staticmethod
    def sort_2nd_version(l):
        '''
        Notice: this method will not work for numpy arrays,
        since they have fixed size and you cannot delete their items.
        '''
        N = len(l)
        for i in xrange(N):
            j = i
            current = l[i]
            while j > 0 and current < l[j - 1]:
                j -= 1
            del l[i]
            l.insert(j, current)

    @staticmethod
    def sort(l):
        '''
        Improved insertion sort.
        Move a range of elements in a single operation.
        '''
        for i in xrange(1, len(l)):
            current = l[i]
            for j in xrange(i):
                if l[j] > current:
                    l[j + 1:i + 1] = l[j:i]
                    l[j] = current
                    break


if __name__ == '__main__':
    args = docopt(__doc__)
    l = [int(i) for i in args['<n>']]
    Insertion.sort(l)
    print('Result: {}\nSorted: {}'.format(l, is_sorted(l)))
