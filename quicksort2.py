def partition(arr,low,high):
	pivot_value=arr[low]
	i=low
	j=high
	# goal move all above pivot_value to right
	# goal move all below pivot_value to left
	while i < j:
		while i < high and arr[i] <= pivot_value:
			i+=1
		while arr[j] > pivot_value:
			j-=1
		if i < j:
			#swap i,j
			arr[i],arr[j]=arr[j],arr[i]
	arr[low]=arr[j]
	arr[j]=pivot_value
	#return arr
	return j



def quicksort_rec(arr,low,high):
	if high > low:
		pivot_index = partition(arr,low,high)
		quicksort_rec(arr,low,pivot_index-1)
		quicksort_rec(arr,pivot_index+1,high)
	

def quicksort(arr):
	quicksort_rec(arr,0,len(arr)-1)
	

# arr=[5,3,7]
arr=[1,5,3,7,3,2]
# print(partition(arr,0,len(arr)-1))
quicksort(arr)
print(arr)
