#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

rc = ''
for c in dna:
	if c == 'A':   rc = 'T' + rc
	elif c == 'T': rc = 'A' + rc
	elif c == 'C': rc = 'G' + rc
	else:          rc = 'C' + rc
	
print(rc)

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
