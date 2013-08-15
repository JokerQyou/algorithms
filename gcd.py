#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''欧几里德算法演示，计算两个数的最大公约数'''

import sys

def gcd(p, q):
	if q == 0:
		return p
	r = int(p % q)
	return gcd(q, r)

if len(sys.argv) == 3:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print gcd(a, b)

