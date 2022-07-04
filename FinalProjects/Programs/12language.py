"""
Plausible Elvish
When writing fantasy novels, authors must somehow come up with new names that sound like they come from a different language. Make a language generator using Nth-order Markov models. For example, generate Evlish words from a mixture of Finnish and Welsh (or whatever you think Elvish is supposed to look like).

Read books (e.g. Gutenberg Project) into tables of letter frequencies
Generate new words from the tables of frequencies
"""

import random


def find_i(arr, target):
	for i in range(len(arr)):
		if arr[i][0] == target:
			return i
	return -1

def find_and_add(arr, c):
	ci = find_i(one, c)
	if ci < 0:
		new_c = [c, 0]
		one.append(new_c)
		one[ci][1] += 1

FILE = "/home/andrwchu/Work/FinalProjects/Data/en.txt"

f = open(FILE)

one = []  # list of [c, freq]
two = []  # list of [c - 1, list of [c, freq]]
three = []  # list of [c - 2, list of [c - 1, list of [c, freq]]]

count1 = 0
count2 = 0
count3 = 0

lines = f.readlines()

for i in range(len(lines) - 1):
	line = lines[i].replace("\n", " ")
	length = len(line)  # length of original line

	line = lines[i - 1].replace("\n", " ")[-2:] + line  # prepend previous line
	line = line.lower()
	if(i<5): print(line)

	for j in range(2, len(line)):
		c = line[j]
		c1 = line[j - 1]
		c2 = line[j - 2]

		ci = find_i(one, c)
		if ci < 0:
			new_c = [c, 0]
			one.append(new_c)
		one[ci][1] += 1


print(one)
