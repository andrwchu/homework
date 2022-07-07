
# p3 51sw.py -a GGTTGACTA -b TGTTACGG --add 3 --sub 3 --gap 2

import argparse

def s(ai, bj, add, sub):
	if ai == bj:
		return add
	else:
		return -sub


parser = argparse.ArgumentParser(description="Smith-Waterman Algorithm")
parser.add_argument(
	"-a", required=True, type=str, metavar="<str>", help="required string argument"
)
parser.add_argument(
	"-b", required=True, type=str, metavar="<str>", help="required string argument"
)
parser.add_argument(
	"--add", required=True, type=int, metavar="<int>", help="required integer argument"
)
parser.add_argument(
	"--sub", required=True, type=int, metavar="<int>", help="required integer argument"
)
parser.add_argument(
	"--gap", required=True, type=int, metavar="<int>", help="required integer argument"
)
arg = parser.parse_args()

a = arg.a
b = arg.b
add = arg.add
sub = arg.sub
gap = arg.gap

# initalize H and pointer arrays
H = []  # a seq : i rows, b seq : j cols
pointers = []
for row in range(len(a) + 1):
	if row == 0:
		H.append([0] * (len(b) + 1))
	else:
		col = [None] * len(b)
		col.insert(0, 0)  # first column of zeros
		H.append(col)
	pointers.append([[-1, -1] for i in range(len(b) + 1)])


max_i = 0
max_j = 0
max_val = H[0][0]

for j in range(1, len(H[0])):
	for i in range(1, len(H)):
		# calculate score
		diag = H[i - 1][j - 1] + s(
			a[i - 1], b[j - 1], add, sub
		)  # offset for a and b bc 1-indexed
		left = H[i][j - 1] - gap
		up = H[i - 1][j] - gap
		score = max(diag, up, left, 0)
		H[i][j] = score

		max_pointers =[]
		# update pointers
		if score == diag:
			pointer = [i - 1, j - 1]
		elif score == up:
			pointer = [i - 1, j]
		elif score == left:
			pointer = [i, j - 1]
		else:
			pointer = [-1, -1]
		pointers[i][j] = pointer

		# check for max score
		if score > max_val:
			max_i = i
			max_j = j
			max_val = H[max_i][max_j]

print(H[max_i][max_j])

a_list = []
b_list = []

next_i = -1
next_j = -1

seq_score = 0

while H[max_i][max_j] > 0:
	seq_score += H[max_i][max_j]

	# find next location
	pointer = pointers[max_i][max_j]

	next_i = pointer[0]
	next_j = pointer[1]


	print([max_i, max_j])
	if next_i == max_i:
		a_list.insert(0, a[max_i - 1])
		b_list.insert(0, "-")
	elif next_j == max_j:
		a_list.insert(0, "-")
		b_list.insert(0, b[max_j - 1])
	else:
		a_list.insert(0, a[max_i - 1])
		b_list.insert(0, b[max_j - 1])

	max_i = next_i
	max_j = next_j

for r in H:
	print(r)

print(a_list)
print(b_list)
print(seq_score)

# TODO detect multiple paths for pointers, might need to create a recursive function
# https://vlab.amrita.edu/?sub=3&brch=274&sim=1433&cnt=1
