def binarysearch(A,key):
	print('searching',A,'for',key, 'len(A)', len(A))
	low=0
	high=len(A)-1
	iterations=0

	while low <= high:
		mid=low + (high-low)//2
		print('test',A[mid])
		iterations+=1
		if A[mid]==key:
			return (mid,'iterations:'+str(iterations))
		elif A[mid] < key:
			low=mid+1
		else:
			high=mid+1
	return (-1,'iterations:'+str(iterations))

A=[1,3,5,7]
print(binarysearch(A,5))

A=[1,3,5,7,9,11]
print(binarysearch(A,11))
