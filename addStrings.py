def multiply(a,b):
	a="".join(reversed(a))
	b="".join(reversed(b))
	return a,b


# print(multiply('997','88111'))

def add(a,b):
	if len(a)>len(b):
		# add 0 to beginning of b
		b = '0'*(len(a)-len(b))+b
	else:
		a = '0'*(len(b)-len(a))+a
	print(a,b)
	a=list(reversed(a))
	b=list(reversed(b))
	carry=0
	result=[]
	for i in range(len(a)):
		digit = (int(a[i])+int(b[i])+carry)%10
		print('digit',digit)
		result.append(str(digit))	
		carry = (int(a[i])+int(b[i])+carry)//10
		print('carry',carry)
	result.append(str(carry))

	return "".join(reversed(result))

print(add('999997','99988111'))
# print(add('9','1'))
# print(add('99','1'))
