'''
Genome data is often described as a feature, which is just a part of a chromosome with a specific location. An exon is a feature, as is a SNP, or a ChIP-seq peak. Sometimes people ask "which exons overlap known mutations?" Write a couple programs that make these comparisons and note the difference in resources (time, CPU) required.

Make a random feature generator
Implement some feature comparison functions
Simple lists
Dictionaries
Sorted lists
Compare time, memory, and programming effort

'''

import math
import random

def rand_feature(num, max_index, median_len, range_len, name):
	features = []
	for i in range(num):
		len = median_len + random.randint(-range_len, range_len)
		len = abs(len)
		
		a = random.randint(0, max_index - len)
		b = a + len
		
		feature = [name, a, b]
		features.append(feature)
	return features
		
	
fa = rand_feature(10, 1000, 100, 100, 'exons')
fb = rand_feature(15, 500, 100, 50, 'SNP')
fc = rand_feature(15, 2000, 1000, 1000, 'peak')
F = [fa, fb, fc]
extract_start_end(F)

print(F)
