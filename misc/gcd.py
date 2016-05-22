#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from docopt import docopt

__doc__ = '''
gcd

Usage:
    gcd [<x> <y>]

Options:
    -h --help  Show this help
'''

def gcd(p, q):
	if q == 0:
		return p
	r = int(p % q)
	return gcd(q, r)

if __name__ == '__main__':
    args = docopt(__doc__)
    print(gcd(int(args['<x>']), int(args['<y>'])))
