#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

nums = [int(x) for x in sys.argv[1:]]
nums.sort()

count = len(nums)
sum = 0
for i in nums:
	sum += i
mean = sum / count

print(f'Count: {count}')
print(f'Min: {nums[0]}')
print(f'Max: {nums[count - 1]}')
print(f'Mean: {mean:.3f}')

SDsum = 0
for s in nums:
	i = int(s)
	SDsum += (i - mean)**2
print(f'SD: {(math.sqrt(SDsum / count)):.3f}')


if count % 2 == 1:
	print(f'Median: {(nums[count // 2]):.3f}')
else:
	print(f'Median: {((nums[count // 2 - 1] + nums[count // 2])/2):.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
