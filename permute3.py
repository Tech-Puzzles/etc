#O(n!) time complexity
#O(1) space complexity
def permute(arr,start):
	print('='*start*1,end="")
	print('stack call permute(',arr,start,')')
	if start == len(arr) -1:
		print('answer',arr)
	for i in range(start,len(arr)):
		#swap
		arr[i],arr[start]=arr[start],arr[i]
		# n!
		#recurse
		permute(arr,start+1)
		# swap back
		arr[i],arr[start]=arr[start],arr[i]

	print('='*start*1,end="")
	print('return',arr,start)

permute([1,2,3,4,5],0)
