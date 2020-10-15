class Node:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data
	def __str__(self):
		#pass	
		return inorder(self);
		


def insert(root,data):
	if root is None:
		return Node(data)
	else:
		if root.data == data:
			#return root
			pass
		elif root.data > data:
			root.left = insert(root.left, data)
			#return root
		elif root.data < data:
			root.right = insert(root.right, data)
			#return root
	# never reach?
	print('XXX',root)
	return root

def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.data)
		inorder(root.right)
	return ""

def preorder(root):
	if root is not None:
		print(root.data)
		preorder(root.left)
		preorder(root.right)
	return ""

def postorder(root):
	if root is not None:
		postorder(root.left)
		postorder(root.right)
		print(root.data)
	return ""

tree=insert(None,10)
tree=insert(tree,6)
tree=insert(tree,20)
tree=insert(tree,1)
tree=insert(tree,1)
tree=insert(tree,1)

# print(tree)
# postorder(tree)
inorder(tree)
