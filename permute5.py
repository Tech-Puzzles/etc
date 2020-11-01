def permute(arr,start):
	if start == len(arr)-1:
		print(arr)
	else:
		for i in range(start,len(arr)):
			# swap
			arr[i],arr[start]= arr[start],arr[i]
			permute(arr,start+1)
			# swap back
			arr[i],arr[start]= arr[start],arr[i]
# permute([2,1],0)
# permute([3,2,1],0)
# permute([4,3,2,1],0)
permute([1,2],0)
permute([1,2,3],0)
permute([1,2,3,4],0)
