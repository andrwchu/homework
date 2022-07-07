"""
Genome data is often described as a feature, which is just a part of a chromosome with a specific location. An exon is a feature, as is a SNP, or a ChIP-seq peak. Sometimes people ask "which exons overlap known mutations?" Write a couple programs that make these comparisons and note the difference in resources (time, CPU) required.

Make a random feature generator
Implement some feature comparison functions
Simple lists
Dictionaries
Sorted lists
Compare time, memory, and programming effort

"""

import math
import random


def gen_len(med, ran):
	length = 0
	while length == 0:
		length = med + random.randint(-ran, ran)
		length = abs(length)
	return length


def rand_feature(num, median_len, range_len, chrm):
	features = []
	cursor = 0
	for i in range(num):

		out_length = gen_len(median_len, range_len)
		cursor += out_length

		feat_length = gen_len(median_len, range_len)

		a = cursor
		b = a + feat_length
		cursor = b

		feature = [random.choice(chrm), a, b]
		features.append(feature)

	features = sorted(features, key=lambda x: x[0])
	return features


def process(feat_lists):
	chrm_dict = {}
	for name, feat_list in feat_lists:
		for feat in feat_list:
			# feat in form of [chrm, start, end]
			chrm = feat[0]
			start = feat[1]
			end = feat[2]

			# marker in form of [currentPos, linkPos, isStart, name]
			marker1 = [start, end, True, name]
			marker2 = [end, start, False, name]

			if chrm not in chrm_dict:
				chrm_dict[chrm] = []
			chrm_dict[chrm].append(marker1)
			chrm_dict[chrm].append(marker2)

	for k in chrm_dict.keys():
		chrm_dict[k] = sorted(chrm_dict[k], key=lambda x: x[0])
		yield (k, chrm_dict[k])


fa = ["exon", rand_feature(4, 5, 5, ["I", "II"])]
fb = ["SNP", rand_feature(4, 5, 5, ["I", "II"])]
fc = ["peak", rand_feature(4, 5, 5, ["I", "II"])]

F = [fb, fc, fa]

for f in F:
	print(f[0], f[1])

for k, markers in process(F):
	print(markers)

	opened = []
	for i in markers:
		if i[2]:
			for j in opened:
				ref_start, ref_end = i[0], i[1]
				comp_start, comp_end = j[0], j[1]

				if comp_start <= ref_start <= comp_end:
					print(f"{k}\t{ref_start}\t{comp_end}\t{j[3]}-{i[3]}")

			opened.append(i)

		else:
			search = [i[1], i[0], not i[2], i[3]]
			if search in opened:
				opened.pop(opened.index(search))
