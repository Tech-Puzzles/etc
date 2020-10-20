def partition(arr,low,high):
	pivot=arr[low]
	i=low
	j=high
	while i < j:
		while i < high and arr[i] <= pivot:
			i+=1
		while arr[j] > pivot:
			j-=1
		if i<j:
			#swap
			arr[i],arr[j] = arr[j],arr[i]

	arr[low]=arr[j]
	arr[j]=pivot
	return j


def quicksort_rec(arr, low, high):
	if low < high:
		pivot_index=partition(arr,low,high)
		quicksort_rec(arr, low, pivot_index-1)
		quicksort_rec(arr, pivot_index+1,high)


def quicksort(arr):
	quicksort_rec(arr,0,len(arr)-1)
	print(arr)

arr=[5,1,7,3,10]
quicksort(arr)
