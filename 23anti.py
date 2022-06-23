#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

s = ''
for i in dna:
	if i == 'A':
		s = 'T' + s
	elif i == 'T':
		s = 'A' + s
	elif i == 'C':
		s = 'G' + s
	else:
		s = 'C' + s
	
print(s)

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
