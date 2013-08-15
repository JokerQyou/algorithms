#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

class Algorithm(object):
	"""排序算法模板"""
	def __init__(self, arg):
		super(Algorithm, self).__init__()
		self.arg = arg
		self.sort(self.arg)
		print self.isSorted(self.arg)
		self.show(self.arg)

	def sort(self, arg):
		pass

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
	sort = Algorithm(argvs)
if __name__ == '__main__':
	main()