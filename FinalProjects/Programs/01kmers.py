import mcb185

def gen_perms(layer, k_list):  # layer is 0-indexed
	BASES = "ATGC"

	if layer < 0:
		return k_list

	# rotation controls how often bp changes (ATGC vs AAAATTTTGGGGCCCC)
	rotation = 4 ** layer
	b_pos = 0
	for i in range(len(k_list)):
		k_list[i] += BASES[b_pos]

		rotation -= 1
		if rotation == 0:
			b_pos = (b_pos + 1) % 4
			rotation = 4 ** layer

	return gen_perms(layer - 1, k_list)


def missing_kmer(seq, k):
	k_list = gen_perms(k - 1, [""] * 4 ** k)
	for i in range(len(seq) - (k - 1)):
		kmer_i = seq[i : i + k]
		if kmer_i in k_list:
			search = k_list.index(kmer_i)
			# print(kmer_i, search)
			if search >= 0:
				k_list.pop(search)
	return k_list

k = 6
file1 = "/home/andrwchu/Work/FinalProjects/Data/chr1.fa"
for name, seq in mcb185.read_fasta(file1):
	print(missing_kmer(seq, k))
