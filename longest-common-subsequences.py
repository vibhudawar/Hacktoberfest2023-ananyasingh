def longestCommonSubsequence(text1, text2):
	n = len(text1)
	m = len(text2)

	# Initializing two lists of size m
	prev = [0] * (m + 1)
	cur = [0] * (m + 1)

	for idx1 in range(1, n + 1):
		for idx2 in range(1, m + 1):
			# If characters are matching
			if text1[idx1 - 1] == text2[idx2 - 1]:
				cur[idx2] = 1 + prev[idx2 - 1]
			else:
				# If characters are not matching
				cur[idx2] = max(cur[idx2 - 1], prev[idx2])

		prev = cur.copy()

	return cur[m]

if __name__ == '__main__':
	S1 = "AGGTAB"
	S2 = "GXTXAYB"

	# Function call
	print("Length of LCS is", longestCommonSubsequence(S1, S2))
# This code is contributed by Rishabh Mathur
