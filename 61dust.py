#!/usr/bin/env python3
# 61dust.py

import argparse
import math

import mcb185

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='fasta file statistics.')
parser.add_argument('--f', required=True, type=str,
	metavar='<str>', help='required string argument')
parser.add_argument('--size', required=True, type=int,
	metavar='<int>', help='required integer argument')
parser.add_argument('--bits', required=True, type=float,
	metavar='<float>', help='required floating point argument')
parser.add_argument('--hard', default=False, action='store_true', help='optional boolean flag')
arg = parser.parse_args()

# https://drive5.com/usearch/manual/masking.html

def entropy(char_dict):
	symbols = len(char_dict.keys())
	freqs = char_dict.values()

	bits = 0
	for freq in freqs:
		p = freq / symbols
		bits -= p * math.log(p, 2)
	return bits

def frequency(seq):
	char_dict = {}
	for c in seq:
		if c not in char_dict: char_dict[c] = 0
		char_dict[c] += 1

	return char_dict

file  = arg.f
window = arg.size
min_bits = arg.bits
soft_mask = not arg.hard
for name, seq in mcb185.read_fasta(file):
	print('>' + name)
	masked_seq = ''
	if window > len(seq):
		print(seq)
		continue

	# use cursor to make sure entire window is masked and not overwritten
	cursor = 0
	for i in range(len(seq) - window):
		if not cursor == i: continue

		char_dict = frequency(seq[i:i + window])
		if entropy(char_dict) < min_bits:
			if soft_mask:
				masked_seq = masked_seq[:i] + seq[i:i + window].lower()
			else:
				masked_seq = masked_seq[:i] + 'N' * window
			cursor += window
		else:
			masked_seq = masked_seq[:i] + seq[i:i + window]

		cursor += 1

	print(masked_seq)
