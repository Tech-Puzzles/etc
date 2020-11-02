class Node:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data

	def __str__(self):
		return inorder(self)


def insert(root,data):
	if root is None:
		return Node(data)
	else:
			if root.data == data:
				pass
			elif data < root.data:
				root.left = insert(root.left, data)
			else:
				root.right = insert(root.right, data)
	return root

def inorder(root):	
	if root is not None:
			inorder(root.left)
			print(root.data)
			inorder(root.right)
	return ""

root=None
root=insert(root,2)
root=insert(root,1)

print(root)

