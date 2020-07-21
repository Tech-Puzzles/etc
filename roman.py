modlist=[ (1000,'M'),(500,'D'), (100,'C'),(50,'L'), (10,'X'),(5,'V'), (1,'I')]

def roman(N):
	answer=""
	print('input',N)
	for item in modlist:
		print('\n>>>',item[1])
		print(int(N/item[0]))
		print(item[1]*int(N/item[0]),end="")
		answer+=(item[1]*int(N/item[0]))
		N=N%item[0]
		if N==0:
			break
	return answer
print('\n'+roman(3999))
