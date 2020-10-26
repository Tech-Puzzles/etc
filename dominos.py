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
def findpairs(arr,target):
	hash={}
	# O(n)
	for x,y in arr:
		hash[(x,y)]=1
		hash[(y,x)]=1
	
	# O(n)
	for x,y in arr:
		# O(1)
		if (target-x,target-y) in hash:
			#print((x,y), hash[(target-x,target-y)])
			print((x,y), (target-x,target-y))

findpairs([(0,3), (2,4), (4,1), (5,2) ], 5)
