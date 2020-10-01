# assume root at 0th index
# bubble up
arr=[10,9]

def heap_insert(arr,k):
	arr.append(k)
	i=len(arr)-1
	parent=(i-1)//2
	while i != 0 and arr[i] > arr[parent]:
		# swap
		arr[i] , arr[parent] = arr[parent] , arr[i]
		i=parent	
		parent=(i-1)//2

heap_insert(arr,12)
print(arr)
heap_insert(arr,0)
print(arr)
heap_insert(arr,20)
print(arr)
