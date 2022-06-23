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
for i in range(30):
	r = random.randint(1, 100)
	if(r<=60):
		if(r%2==0):
			s += 'A'
		else:
			s += 'T'
		sum+=1
	else:
		if(r%2==0):
			s += 'G'
		else:
			s += 'C'
			
print(len(s), sum / len(s), s)


"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
