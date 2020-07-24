def grow(i, input):
	# left
	for j in range(i-1,-1,-1):
		print('left',input[j], input)
	# right
	for j in range(i+1,len(input),+1):
		print('right',input[j], input)
	return input[i]
	

def maxarea(input):
	max1=0
	for i in range(len(input)):
		print('START',i, input)
		max1 = max(grow(i, input), max1)

print(maxarea([6,2,4,5,4,3,1]))
