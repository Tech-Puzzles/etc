class Node:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data

def insert(root,data):
	if root is None:
		return Node(data)
	else:
		if root.data == data:
			pass
		elif data < root.data:
			root.left = insert(root.left,data)
		else:
			root.right = insert(root.right,data)
	return root

tree=insert(None,10)
tree=insert(tree,4)
tree=insert(tree,2)
tree=insert(tree,1)

def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.data)
		inorder(root.right)

inorder(tree)
