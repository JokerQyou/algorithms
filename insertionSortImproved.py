#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

class Insertion(object):
	"""排序算法模板"""
	def __init__(self, arg):
		super(Insertion, self).__init__()
		self.arg = arg
		self.sort(self.arg)
		print self.isSorted(self.arg)
		self.show(self.arg)

	def sort(self, arg):
		N = len(arg)
		i = 0
		while i != N:
			j = i
			while j != 0 and arg[j - 1] >= arg[i]:
				j = j - 1
			value = arg[i]
			del arg[i]
			arg.insert(j, value)
			i = i + 1

	def isSorted(self, arg):
		for x in xrange(1, len(arg)):
			if arg[x] < arg[x - 1]:
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
	sort = Insertion(argvs)
if __name__ == '__main__':
	main()