# Given two sequences, find the length of longest subsequence present in both of them. 
# A subsequence is a sequence that appears in the same relative order, 
# but not necessarily contiguous.


def longestCommonSub(X, Y):
	n = len(X)
	m = len(Y)
	mat = [[0 for _ in range(m)]for __ in range(n)]

	maxLen = 0

	for i in range(n):
		for j in range(m):
			if X[i] == Y[j]:
				prev = mat[i-1][j-1] if i-1>=0 and j-1>=0 else 0
				mat[i][j] = prev + 1
			else:
				a = mat[i-1][j]  if i-1>=0 else 0
				b = mat[i][j-1]  if j-1>=0 else 0
				mat[i][j] = max(a, b)
			maxLen=max(maxLen, mat[i][j])
			print(X[i],Y[j], mat[i][j],maxLen)
	print(mat)
	return maxLen

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", longestCommonSub(X, Y))
