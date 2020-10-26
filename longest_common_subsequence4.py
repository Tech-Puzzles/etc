def lcs(X,Y):
	m=len(X)
	n=len(Y)

	L=[]
	for _ in range(m+1):
		L.append([0]*(n+1))

	#print(L)
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				pass
			elif X[i-1] == Y[j-1]:
				L[i][j] = 1 + L[i-1][j-1]
			else:
				L[i][j] = max(L[i-1][j],L[i][j-1])
	return L[m][n]


X="XABXABXAB"
Y="XAB"
print(lcs(X,Y))
		
