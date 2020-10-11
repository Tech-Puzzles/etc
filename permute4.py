def permute(arr,start):
	if start == len(arr)-1:
		print(arr)
	for i in range(start,len(arr)):
		#swap i, start
		arr[i],arr[start]=arr[start],arr[i]
		#recurse at start+1
		permute(arr.copy(),start+1)
		#swap back call by reference

#permute([1,2,3],0)
permute([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],0)
