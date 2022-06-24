#!/usr/bin/env python3

import random
# random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

s = ''
sum = 0
seq_len = 30
percent = 0.60

for i in range(seq_len):
	r = random.random()
	if(r < percent):
		s += random.choice('AT')
		sum += 1
	else:
		s += random.choice('GC')
	
			
print(seq_len, sum / len(s), s)


"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
