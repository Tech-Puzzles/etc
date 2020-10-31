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
def dominos(arr,target):
	#both x1+x2 must = target and y1+y2 must = target
	hash={}
	result=[]
	arr2=[]
	for x,y in arr:
		arr2.append((y,x))
	arr.extend(arr2)	
	for x,y in arr:
		hash[(x,y)] = True
	
	for x,y in arr:
		if (target - x,target-y) in hash:
			print((target-x,target-y),(x,y))
			result.append([(target-x,target-y),(x,y)])
	print('result',result)
	return result

# dominos([ (0,3), (2,4), (4,1), (5,2)] ,5)

def runTest(arr,target,expect):
	ret=dominos(arr,target)	
	"""
	for item in ret:
		print('ret',item)
	for item in expect:
		print('expect',item)
	for i in range(len(ret)):
		print('compare item',ret[i]==expect[i])
	"""
	print('compare','ret',ret,'expect',expect,ret==expect)
	# print('cmp','ret',ret,'expect',expect,((ret > expect)-(ret < expect)))
	print('pass' if ret==expect else 'fail')
	

runTest([ (0,3), (2,4), (4,1), (5,2)] ,5, [[(5, 2), (0, 3)], [(1, 4), (4, 1)], [(0, 3), (5, 2)], [(2, 5), (3, 0)], [(4, 1), (1, 4)], [(3, 0), (2, 5)]])
