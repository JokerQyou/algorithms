#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import time

def toNumber(a):
	try:
		a = int(a)
	except Exception, e:
		a = float(a)
	return a

def main():
	if len(sys.argv) == 3:
		filename = sys.argv[1]
		algorithm = sys.argv[2]
		with open(filename) as f:
			L = [toNumber(x) for x in f.readlines()]
		tStart = time.time()
		if algorithm == 'selection':
			import selectionSort
			class Selection(selectionSort.Selection):
				"""重载选择排序类的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			sort = Selection(L)
		elif algorithm == 'insertion':
			import insertionSort
			class Insertion(insertionSort.Insertion):
				"""重载插入排序类的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			sort = Insertion(L)
		elif algorithm == 'shell':
			import shellSort
			class Shell(shellSort.Shell):
				"""重载希尔排序类的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			sort = Shell(L)
		tEnd = time.time()
		print ('%s algorithm took %f second(s) to sort %d number(s).')%(algorithm, tEnd - tStart, len(L))

if __name__ == '__main__':
	main()