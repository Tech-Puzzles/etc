def counting_sort(arr):
	max1 = max(arr)+1
	buckets={}
	for i in arr:
		if i in buckets:
			buckets[i]+=1
		else:
			buckets[i]=1
		
	#print(max1)
	print(buckets)
	for i in range(max1):
		#print('i',i)
		if i in buckets:
			for _ in range(buckets[i]):
				print(i, end=" ")


counting_sort([1,2,10000,100,100,3])
