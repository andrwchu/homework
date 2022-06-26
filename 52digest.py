#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments


# EcoRI: cuts DNA at pattern (i.e. g/cut/aattc)


def count_misc_chars(char_pat, str):
	sum_len = 0
	for i in re.finditer(char_pat, str):
		sum_len += len(i.group())
	return sum_len

pat_in = sys.argv[2]
inter = '\s*\d*\s*' # ignore line numbers and spaces
pat = ''
for i in range(0, len(pat_in) - 1):
	pat += pat_in[i] + inter
pat += pat_in[-1]

f = open(sys.argv[1])
file = f.read()

start = re.search('(ORIGIN\s*1\s*)([acgt])', file)
indices = [start.start(2)] # first base
misc_chars = []
for match in re.finditer(pat, file):
	index = match.start()
	misc_char = count_misc_chars(inter, file[indices[-1]:index])
	
	indices.append(index)
	misc_chars.append(misc_char)
	
for i in range(len(indices) - 1):
	print(indices[i + 1] - indices[i] - misc_chars[i])
f.close()


"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
