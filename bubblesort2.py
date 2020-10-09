def bubblesort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j+1] < arr[j]:
				#swap j,j+!
				arr[j+1] , arr[j] = arr[j] , arr[j+1]
	return arr


print(bubblesort([4,5,6,7,1]))
print(bubblesort([10,4,5,6,7,1]))
			


