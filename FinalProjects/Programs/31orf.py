import argparse
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


def pick_longest(orfs):
	max_len = -1
	max_i = -1
	for i in range(len(orfs)):
		orf_len = len(orfs[i])
		if orf_len > max_len:
			max_len = orf_len
			max_i = i

	if max_i < 0:
		return ""
	return orfs[max_i]


parser = argparse.ArgumentParser(description="longest open reading frame")
parser.add_argument(
	"--f", required=True, type=str, metavar="<str>", help="required string argument"
)
parser.add_argument(
	"--three", default=False, action="store_true", help="optional boolean flag"
)
parser.add_argument(
	"--six", default=False, action="store_true", help="optional boolean flag"
)
arg = parser.parse_args()

seq_file = arg.f
six = arg.six
three = arg.three
if six:
	three = True

for name, seq in mcb185.read_fasta(seq_file):
	for i in range(3):
		if (i == 1 or i == 2) and not three:
			continue
		orfs = get_orfs(seq, i)
		longest = pick_longest(orfs)
		print(f" Forward {i + 1} Frame: {len(longest)}\n{longest}")

	seq = seq[::-1]

	for i in range(3):
		if not six:
			continue
		longest = pick_longest(orfs)
		print(f" Backward {i + 1} Frame: {len(longest)}\n{longest}")
