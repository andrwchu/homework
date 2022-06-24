#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Give them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

numPeople = 25
trials = 10000;

sum = 0
for x in range(trials):
	calendar = [0 for x in range(0,365)]
	
	for i in range(numPeople):
		calendar[random.randint(0, 364)] += 1
	
	for b in calendar:
		if b > 1:
			sum += 1
			break
			
print(f'{(sum / trials):.3f}')

"""
python3 33birthday.py
0.571
"""

