#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

sum = 0;
for i in range(len(dna)):
	if dna[i] == 'G' or dna[i] == 'C':
		sum += 1
		
print('%.2f' % (sum / len(dna))) 
print('{:.2f}'.format(sum / len(dna)))
print(f'{(sum / len(dna)):.2f}') # fstring format

"""
python3 21gc.py
0.42
0.42
0.42
"""
