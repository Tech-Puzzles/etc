def heapify(arr,i):
	largest=i
	left=i*2+1
	right=i*2+2
	if left < len(arr) and arr[left] > arr[largest]:
		largest=left
	if right < len(arr) and arr[right] > arr[largest]:
		largest=right
	if largest != i:
		#swap i , largest
		arr[i],arr[largest]= arr[largest], arr[i]
		heapify(arr,largest)
	

arr=[1,2,3,4,5]

for i in reversed(range(len(arr)//2)):
	heapify(arr,i)

print(arr)
