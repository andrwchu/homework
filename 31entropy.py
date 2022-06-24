#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

probabilities = [float(x) for x in sys.argv[1:]]

Hsum = 0
for i in probabilities:
	Hsum += (i * math.log(i, 2)) # to calculate shannons, need to use log base 2
print(f'{(Hsum * -1):.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
