#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

size = int(sys.argv[1])
number = int(sys.argv[2])
length = int(sys.argv[3])

coverage = [0] * size
for i in range(number):
	start = random.randint(0, size - length)
	for j in range(length):
		coverage[start + j] += 1

coverage = coverage[length - 1: -(length - 1)]


average = sum(coverage) / len(coverage)

print(f'{min(coverage)} {max(coverage)} {average:.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
