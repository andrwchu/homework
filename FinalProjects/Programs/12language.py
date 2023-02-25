"""
Plausible Elvish
When writing fantasy novels, authors must somehow come up with new names that sound like they come from a different language. Make a language generator using Nth-order Markov models. For example, generate Evlish words from a mixture of Finnish and Welsh (or whatever you think Elvish is supposed to look like).

Read books (e.g. Gutenberg Project) into tables of letter frequencies
Generate new words from the tables of frequencies
"""

import random
import re


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


def clean_line(s):
	s = re.sub(r"[\d*_]", "", s)
	s = re.sub(r"[^\w\s]", "", s)
	s = s.replace("\n", " ")

	s = s.lower()
	return s

def recurse(arr, target_arr):
	target = target_arr[0]



FILE = "/home/andrwchu/Work/homework/FinalProjects/Data/en.txt"

f = open(FILE)

one = []  # list of [c, freq]
two = []  # list of [c - 1, list of [c, freq]]
three = []  # list of [c - 2, list of [c - 1, list of [c, freq]]]

count1 = 0
count2 = 0
count3 = 0

lines = f.readlines()

for i in range(len(lines) - 1):
	line = clean_line(lines[i])
	line1 = clean_line(lines[i - 1])
	length = len(line)  # length of original line

	line = line1[-2:] + line  # prepend previous line

	for j in range(2, len(line)):
		c = line[j]
		c1 = line[j - 1]
		c2 = line[j - 2]

		ci = find_i(one, c)
		if ci < 0:
			new_c = [c, 0]
			one.append(new_c)
		one[ci][1] += 1

		ci2 = find_i(two, c1)
		if ci2 < 0:
			new_ci2 = [ci, [c, 0]]
			two.append(new_ci2)

		ifci
print(one)
