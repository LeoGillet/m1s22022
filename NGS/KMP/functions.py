def file_to_string(filename):
	with open(filename, 'r') as f:
		seq = f.readlines()
		return seq[0]

def naive_matcher(file: str, pat: str):
	seq = file_to_string(file)
	occurences = []
	char_comps = shift = 0
	len_pat = len(pat)
	len_seq = len(seq)
	for index in range(len_seq-1):
		found = False
		while seq[index+shift] == pat[0+shift] and not found:
			if shift == len_pat-1:
				print(f'Pattern found in sequence (index : {index})')
				occurences.append(index)
				shift = 0
				found = True
			print('Comparing', seq[index:1+index+shift], 'with', pat[0:1+shift])
			shift += 1
			char_comps += 1
			if index+shift > len_seq-1:
				return char_comps, len(occurences)
		shift = 0
	return char_comps, len(occurences)

# pattern = 'ATAGTGCAT'
def compute_prefix_table(pat):
	bestp = []
	[bestp.append(0) for i in range(len(pat))]
	k = 0
	for q in range(1, len(pat)):
		while k > 0 and pat[k] != pat[q]:
			k = bestp[k-1]
		if pat[k] == pat[q]:
			k += 1
		bestp[q] = k
	return bestp

def kmp_matcher(file: str, pat: str):
	# TODO : n comparaisons trop grand, n occurences 215 =/= 245
	seq = file_to_string(file)
	bestp = compute_prefix_table(pat)
	q = char_comps = occurences = 0
	for i in range(0, len(seq)):
		while q > 0 and pat[q] != seq[i]:
			q = bestp[q]
			char_comps += 1
		if pat[q] == seq[i]:
			q += 1
			char_comps += 1
		if q == len(pat):
			q = bestp[q-1]
			occurences += 1
	return char_comps, occurences






