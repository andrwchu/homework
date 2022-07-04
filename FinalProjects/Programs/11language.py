"""
Plausible Elvish
When writing fantasy novels, authors must somehow come up with new names that sound like they come from a different language. Make a language generator using Nth-order Markov models. For example, generate Evlish words from a mixture of Finnish and Welsh (or whatever you think Elvish is supposed to look like).

Read books (e.g. Gutenberg Project) into tables of letter frequencies
Generate new words from the tables of frequencies
"""

import random


def dict_to_arr(dict):
	word = []
	freq = []
	for k, v in dict.items():
		word.append(k)
		freq.append(v)
	return word, freq


FILE = "/home/andrwchu/Work/FinalProjects/Data/en.txt"

f = open(FILE)

one = {}
two = {}
three = {}

count1 = 0
count2 = 0
count3 = 0

lines = f.readlines()

for i in range(len(lines) - 1):
	line = lines[i]
	length = len(line)  # length of original line

	line += lines[i + 1][:2]
	line = line.lower()
	line = line.replace("\n", " ")

	count1 += length
	count2 += length - 1
	count3 += length - 2

	for j in range(len(line) - 2):
		c1 = line[j]
		if c1 not in one:
			one[c1] = 0
		one[c1] += 1

		c2 = line[j : j + 2]
		if c2 not in two:
			two[c2] = 0
		two[c2] += 1

		c3 = line[j : j + 3]
		if c3 not in three:
			three[c3] = 0
		three[c3] += 1

# not necessary to sort, just for ease of debugging
"""
one = sorted(one.items(), key=lambda x: x[1], reverse=False)
two = sorted(two.items(), key=lambda x: x[1], reverse=False)
three = sorted(three.items(), key=lambda x: x[1], reverse=False)
print(type(one[0]))
"""
word1, freq1 = dict_to_arr(one)
word2, freq2 = dict_to_arr(two)
word3, freq3 = dict_to_arr(three)
print(word1)
print(freq1)

# TODO make dicts into arr, make able to pick val from freqs, start predictions with markov, integrate multi file freqs
c = random.choices(word1, weights=freq1)  # does not work because dict --> arr
# https://docs.python.org/3/library/random.html#random.choices
print(c)
