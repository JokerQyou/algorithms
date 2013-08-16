#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

class Selection(object):
	"""选择排序"""
	def __init__(self, arg):
		super(Selection, self).__init__()
		self.arg = arg
		self.sort(self.arg)
		print self.isSorted(self.arg)
		self.show(self.arg)

	def sort(self, arg):
		N = len(arg)
		for x in xrange(0, N):
			minus = x
			for y in xrange(x + 1, N):
				if self.less(arg[y], arg[minus]):
					minus = y
			self.exch(arg, x, minus)

	def exch(self, arg, i, j):
		arg[i], arg[j] = arg[j], arg[i]

	def less(self, p, q):
		return p < q

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
	sort = Selection(argvs)
if __name__ == '__main__':
	main()