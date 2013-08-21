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
			M = L[:]
		if algorithm == 'selection':
			import selectionSort
			class Selection(selectionSort.Selection):
				"""重载选择排序类的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			tStart = time.time()
			sort = Selection(L)
		elif algorithm == 'insertion':
			import insertionSort
			class Insertion(insertionSort.Insertion):
				"""重载插入排序类的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			tStart = time.time()
			sort = Insertion(L)
		elif algorithm == 'insertionImproved':
			import insertionSortImproved
			class Insertion(insertionSortImproved.Insertion):
				"""重载插入排序的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			tStart = time.time()
			sort = Insertion(L)
		elif algorithm == 'shell':
			import shellSort
			class Shell(shellSort.Shell):
				"""重载希尔排序类的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			tStart = time.time()
			sort = Shell(L)
		elif algorithm == 'all':
			'''Test all algorithms'''

			import selectionSort
			class Selection(selectionSort.Selection):
				"""重载选择排序类的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			tSStart = time.time()
			sort = Selection(L)
			tSEnd = time.time()
			print ('selection algorithm took %f second(s) to sort %d numbers.')%(tSEnd - tSStart, len(L))
			
			L = M[:]
			import insertionSort
			class Insertion(insertionSort.Insertion):
				"""重载插入排序类的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			tIStart = time.time()
			sort = Insertion(L)
			tIEnd = time.time()
			print ('insertion algorithm took %f second(s) to sort %d numbers.')%(tIEnd - tIStart, len(L))

			L = M[:]
			import insertionSortImproved
			class InsertionImproved(insertionSortImproved.Insertion):
				"""重载插入排序的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			tIIStart = time.time()
			sort = InsertionImproved(L)
			tIIEnd = time.time()
			print ('insertionImproved algorithm took %f second(s) to sort %d numbers.')%(tIIEnd - tIIStart, len(L))

			L = M[:]
			import shellSort
			class Shell(shellSort.Shell):
				"""重载希尔排序类的构造函数使其不输出排序结果"""
				def __init__(self, arg):
					self.arg = arg
					self.sort(self.arg)
			tShStart = time.time()
			sort = Shell(L)
			tShEnd = time.time()
			print ('shell algorithm took %f second(s) to sort %d numbers.')%(tShEnd - tShStart, len(L))

			L = M[:]
			tLStart = time.time()
			L.sort()
			tLEnd = time.time()
			print ('list.sort() took %f second(s) to sort %d numbers.')%(tLEnd - tLStart, len(L))

			exit(1)
		elif algorithm == 'list.sort':
			tStart = time.time()
			L.sort()

		tEnd = time.time()
		print ('%s algorithm took %f second(s) to sort %d numbers.')%(algorithm, tEnd - tStart, len(L))

if __name__ == '__main__':
	main()