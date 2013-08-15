#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

class Shell(object):
	"""排序算法模板"""
	def __init__(self, arg):
		super(Shell, self).__init__()
		self.arg = arg
		self.sort(self.arg)
		print self.isSorted(self.arg)
		self.show(self.arg)

	def sort(self, arg):
		N = len(arg)
		h = 1
		while h < N / 3:
			h = 3 * h + 1
		while h >= 1:
			for x in xrange(h, N):
				for y in xrange(x, h, -h):
					if self.less(arg[y], arg[y - h]):
						self.exch(arg, y, y - h)
			h = h / 3

	def exch(self, arg, i, j):
		tmp = arg[i]
		arg[i] = arg[j]
		arg[j] = tmp

	def less(self, p, q):
		return p - q < 0

	def isSorted(self, arg):
		for x in xrange(1, len(arg)):
			if self.less(arg[x], arg[x - 1]):
				return False
			return True

	def show(self, arg):
		for x in arg:
			print x,

def toNumber(a):
	try:
		a = int(a)
	except Exception, e:
		a = float(a)
	return a

def main():
	argvs = sys.argv[1:]
	argvs = [toNumber(x) for x in argvs]
	sort = Shell(argvs)

if __name__ == '__main__':
	main()