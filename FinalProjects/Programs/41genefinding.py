import mcb185

def get_orfs(seq, frame):
	START = ["ATG", "AUG"]
	STOP = ["UAA", "UAG", "UGA", "TAA", "TAG", "TGA"]

	seq = "_" * frame + seq

	orf_list = []
	orf_start = -1

	for i in range(0, len(seq), 3):
		codon = seq[i : i + 3]
		if not len(codon) == 3:
			continue
		if codon in START:
			orf_start = i
		elif orf_start > -1 and codon in STOP:
			orf = seq[orf_start : i + 3]
			orf_list.append(orf)
			if len(orf) == 0:
				print(i)
			orf_start = -1

	return orf_list

for name, seq in mcb185.read_fasta(seq_file):
	orfs = get_orf(seq, i)
	print(orfs)


