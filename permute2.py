def permute(A,start):
	if start==len(A)-1:
		print('answer',A)
	else:
		print('loop',len(A)-start)
		for i in range(start,len(A)):
		#for i in range(len(A)):
			# swap i and start
			A[start],A[i]=A[i],A[start]
			print('swap',start,i)
			print('set',A)
			permute(A,start+1)
			# swap i and start
			A[start],A[i]=A[i],A[start]

# permute([1,2,3],0)
# permute([1,2,3,4,5,6,7,8,9,0],0)
permute([1,2,3,4],0)

