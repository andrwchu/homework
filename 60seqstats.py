#!/usr/bin/env python3
# 60seqstats.py

import argparse
import mcb185

# Write a program that computes statistics about a fasta file (e.g. assembly)
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='fasta file statistics.')
parser.add_argument('--f', required=True, type=str,
	metavar='<str>', help='required string argument')
arg = parser.parse_args()

print(arg.f)

seq_lens = []
for name, seq in mcb185.read_fasta(arg.f):
	seq_lens.append(len(seq))

num_seq = len(seq_lens)
assert(num_seq > 0)

total_len = sum(seq_lens)
ave_len = total_len / num_seq

seq_lens.sort()
min_len = seq_lens[0]
max_len = seq_lens[-1]
if len(seq_lens) % 2 == 0:
	median_len = (seq_lens[num_seq // 2 - 1] + seq_lens[num_seq // 2]) / 2
else:
	median_len = seq_lens[num_seq // 2]
	
# N50 
# https://www.rdocumentation.org/packages/CNEr/versions/1.8.3/topics/N50

n50_sum = 0
n50 = 0
for i in range(num_seq - 1, -1, -1):
	n50_sum += seq_lens[i]
	if(n50_sum >= total_len / 2):
		n50 = seq_lens[i]
		break
	
print(f'Number of Sequences: {num_seq}')
print()
print(f'Total Length: {total_len}')
print(f'Min Length: {min_len}')
print(f'Max Length: {max_len}')
print()
print(f'Average Length: {ave_len}')
print(f'Median Length: {median_len}')
print(f'N50 Length: {n50}')

# print(seq_lens)
