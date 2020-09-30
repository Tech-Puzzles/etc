def heapify(arr,i,n):
	largest=i
	left=i*2+1
	right=i*2+2
	if left < n and arr[left] > arr[largest]:
		largest=left
	if right < n and arr[right] > arr[largest]:
		largest=right
	if largest != i:
		#swap
		arr[i],arr[largest] = arr[largest],arr[i]
		heapify(arr,largest,n)


#arr=[1,2,3,4]
#arr=[1,2,3,4]
arr=[1,2,3,4,5,6,7]
for i in reversed(range(len(arr)//2)):
	heapify(arr,i,len(arr))

print(arr)

		
