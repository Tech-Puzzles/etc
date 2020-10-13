import sys
import itertools

def exponential(n):
	print(n,'T')
	print(n,'F')
	if n == 0:
		return
	exponential(n-1)
	exponential(n-1)

# exponential(int(sys.argv[1]))
	
# table = list(itertools.product([False, True], repeat=4))
# table = list(itertools.product([False, True], repeat=int(sys.argv[1])))
# print(table)


def tablize(n, truths=[]):
    if not n:
        print (truths)
    else:
        for i in [True, False]:
            tablize(n-1, truths+[i])

#tablize(6)


def tablize2(n,truths=[]):
	if n == 0:
		print (truths)
	else:
		for i in [True,False]:
			#tablize2(n-1,[i]+truths)
			tablize2(n-1,truths+[i])
tablize2(3)
