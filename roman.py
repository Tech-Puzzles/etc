modlist=[ (1000,'M'),(900,'CM'),(500,'D'),(400,'CD'), (100,'C'),(90,'XC'),(50,'L'),(40,'XL'), (10,'X'),(9,'IX'),(5,'V'), (4,'IV'), (1,'I')]

def roman(N):
	answer=""
	print('input',N)
	for item in modlist:
#	print('\n>>>',item[1])
#	print(int(N/item[0]))
#	print(item[1]*int(N/item[0]),end="")
		answer+=(item[1]*int(N/item[0]))
		N=N%item[0]
		if N==0:
			break
	return answer
print('\n'+roman(3999))
print('\n'+roman(99))
for i in range(3999):
	print('\n'+roman(i))
