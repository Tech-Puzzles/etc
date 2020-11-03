def longest_common_substring(X,Y):
	m = len(X)
	n = len(Y)
	arr=[]
	for _ in range(m+1):
		arr.append([0]*(n+1))
	
	for i in range(1,m+1):
		for j in range(1,n+1):
			if X[i-1]==Y[j-1]:
				arr[i][j]=arr[i-1][j-1]+1


	return arr


			
#print(longest_common_substring("abc","xbc"))
print(longest_common_substring("aaaabc","xaaaaxbc"))
