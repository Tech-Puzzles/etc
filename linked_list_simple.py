class Node:
	def __init__(self,data):
		self.next=None
		self.data=data
		
	def __str__(self):
		curr=self
		if curr is None:
			return ""
		str1=[str(curr.data)]
		while curr.next != None:
			curr=curr.next
			str1.append('curr.data: %s'%curr.data)
		return "\n".join(str1)


a=Node(1)
b=a.next=Node(2)
c=b.next=Node(3)

# print(Node(1))
print(a)
