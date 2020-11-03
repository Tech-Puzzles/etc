def add(a,b):
	# make the same len
	# reverse
	# 
	a1=list(reversed(a))
	b1=list(reversed(b))

	result=[]
	carry=0
	for i in range(len(a1)):
		digit=(a1[i]+b1[i]+carry)%10
		result.append(digit)
		carry=(a1[i]+b1[i]+carry)//10
	result.append(carry)
	return result

print(add([1,2,3],[9,8,7]))		
	
