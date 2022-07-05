import argparse
import mcb185

"""
In V1, I generated all possible iterations, checked seq for the kmer,
	then popped found pairs.
In V2, I find all kmers from seq first using dictionary, then subtract the found
	from all possible iterations
"""


def found_kmer(seq, k):
	k_list = {}
	missing = 4 ** k

	for i in range(len(seq) - (k - 1)):
		kmer_i = seq[i : i + k]
		if kmer_i not in k_list:
			k_list[kmer_i] = 0
			missing -= 1
		if missing == 0:
			break

	return k_list.keys(), missing


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
	found, missing = found_kmer(seq, k)
	if missing == 0:
		return []

	k_list = gen_perms(k - 1, [""] * 4 ** k)

	for kmer in found:
		if kmer in k_list:
			kmer_i = k_list.index(kmer)
			k_list.pop(kmer_i)
	return k_list


parser = argparse.ArgumentParser(description="missing k-mers")
parser.add_argument(
	"--f", required=True, type=str, metavar="<str>", help="required string argument"
)
parser.add_argument(
	"--show_missing", default=False, action="store_true", help="optional boolean flag"
)
arg = parser.parse_args()

seq_file = arg.f
show_missing = arg.show_missing

for name, seq in mcb185.read_fasta(seq_file):
	k = 1
	while True:
		missing = missing_kmer(seq, k)
		if len(missing) == 0:
			k += 1
		else:
			break

	if show_missing:
		print(missing)
	print(f"{name.split()[0]}:\nk = {k}")
