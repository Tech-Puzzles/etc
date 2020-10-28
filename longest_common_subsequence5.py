def lcs(X,Y):
	m=len(X)
	n=len(Y)

	L = []
	for _ in range(m+1):
		L.append([(0,0,0,'')]*(n+1))
	#print(L)

	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				pass
			elif X[i-1] == Y[j-1]:
				L[i][j] = (1+L[i-1][j-1][0],i-1,j-1,X[i-1])
				#print('match',X[i-1])
			else:
				if 	(L[i-1][j])[0] > (L[i][j-1])[0]:
					L[i][j] = L[i-1][j]
				else:
					L[i][j] = L[i][j-1]
	# traverse the array
	value,i,j,letter = L[m][n]
	print('value',value)
	string=letter
	while True:
		value,i,j,letter = L[i][j]
		string+=letter
		if i == 0 or j == 0:
			break
	print("".join(reversed(string)))


	return L[m][n]

# print(lcs("Noah","Papa"))

print(lcs("mury had a little lamb","mary had a little lamb"))
		
	
