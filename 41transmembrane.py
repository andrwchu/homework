#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix


kd_vals = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
	'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
	'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def KD(region):
	kd_sum = 0
	for c in region:
		if c in kd_vals: kd_sum += kd_vals[c]
	return kd_sum / len(region)

def check_seq(seq, target_len, target_kd, check_proline):
	for i in range(len(seq) - target_len + 1):
		target = seq[i:i + target_len]
		if check_proline and 'P' in target:	
			i += target.index('P') # skip to sections w/o proline
			continue
		if KD(target) > target_kd: return True
	return False

f = open(sys.argv[1])
aa_string = ''
aa_name = ''

for line in f.readlines():
	line = line.strip()
	if len(line) < 1: continue
	if line[0] == '>':
		aa_name = line.split('|')[0]
		aa_name = aa_name[1:] # remove leading '>'
	else:
		aa_string += line # update sequence
		if line[-1] == '*':
			signal_peptide = check_seq(aa_string[:30], 8, 2.5, False)
			hydrophobic_region = check_seq(aa_string[30:], 11, 2.0, True)
			if signal_peptide and hydrophobic_region:
				print(aa_name)
			aa_string = ''
			aa_name = ''
f.close()

"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
