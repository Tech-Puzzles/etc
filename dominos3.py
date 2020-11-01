"""
Given a list of integer pairs (dominos), find if there exist any two that sum to a specific target

Dominos:
(0,3)
(2,4)
(4,1)
(5,2)

target 5  

Output: (0,3)(5,2)

"""
def dominos(list1,target):
	hash={}
	# O(n)
	for x,y in list1:
		hash[(x,y)]=True
	
	for x,y in hash:
		if (target - x, target - y) in hash:
			print((x,y),(target-x,target-y))

dominos( [(0,3), (2,4), (4,1), (5,2)], 5)
