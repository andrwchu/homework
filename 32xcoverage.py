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

chromosome = [0 for x in range(size)]
for i in range(number):
	start = random.randint(0, size - length - 1)
	for j in range(length):
		chromosome[start + j] += 1

currentCoverage = chromosome[0]
coverage = [currentCoverage]
for i in range(1, len(chromosome)):
	if chromosome[i - 1] != chromosome[i]: coverage.append(chromosome[i]) 

# remove ends of chromosome that got 0 coverage
if(coverage[0] == 0): coverage.pop(0)
if(coverage[-1] == 0): coverage.pop(-1)

average = sum(coverage) / len(coverage)

coverage.sort()

print(f'{coverage[0]} {coverage[-1]} {average:.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
