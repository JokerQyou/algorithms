#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class SortBase(object):

    @staticmethod
    def sort(l):
        raise NotImplementedError('Should be implemented in subclass')


def is_sorted(l, descending=False):
    '''Check whether a sequence is sorted'''
    if descending:
        return all(l[i] >= l[i + 1] for i in xrange(len(l) - 1))
    return all(l[i] <= l[i + 1] for i in xrange(len(l) - 1))
