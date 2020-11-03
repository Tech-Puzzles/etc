def multiply(a,b):
	a="".join(reversed(a))
	b="".join(reversed(b))
	return a,b


# print(multiply('997','88111'))

def add(a,b):
	sizea=len(a)
	sizeb=len(b)
	# make len the same with 0's
	if sizea < sizeb:
		# 
		pass
	else:
		#
		pass
	a1=list(reversed(a))
	b1=list(reversed(b))
	carry=0
	result=[]
	for i in range(len(a1)):
		print('digit',a1[i],b1[i])
		digit = (a1[i]+b1[i]+carry) % 10
		result.append(digit)
		carry = (a1[i]+b1[i]+carry) // 10
	result.append(carry)
	return result



print(add([9,1,2],[1,7,8]))
