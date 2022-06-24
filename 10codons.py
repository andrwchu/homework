#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'


for i in range(0, len(dna) -2, 3):
	print(dna[i:i+3])

"""
python3 10codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
