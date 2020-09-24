def permute(A,start):
	if start==len(A)-1:
		print(A)
	else:
		for i in range(start,len(A)):
		#for i in range(len(A)):
			# swap i and start
			A[start],A[i]=A[i],A[start]
			print('swap',start,i)
			permute(A,start+1)
			# swap i and start
			A[start],A[i]=A[i],A[start]

permute([1,2,3,4],0)

