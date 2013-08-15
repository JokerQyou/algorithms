#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import random

def main():
	if len(sys.argv) == 3:
		filename = sys.argv[1]
		N = int(sys.argv[2])
		f = open(filename, 'w')
		for x in xrange(0, N):
			r = random.random()
			f.writelines(str(r) + '\n')
		f.close()

if __name__ == '__main__':
	main()