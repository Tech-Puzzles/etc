from collections import deque

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

# recursive
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if key == root.key:
            return root
        elif key < root.key:
            root.left=insert(root.left,key)
        else: 
            root.right=insert(root.right,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


tree=None
tree=insert(tree,10)
tree=insert(tree,20)
tree=insert(tree,1)
# inorder(tree)

def inorder_iterative(root):
  result = ""
  if root == None:
    return

  stk = deque()
  count = 0

  while (len(stk) != 0 or root != None):
    if root != None:
      stk.append(root)
      root = root.left
      continue

    result += str(stk[-1].key) + " "
    root = stk[-1].right
    stk.pop()
  return str(result)

# arr = [100,50,200,25,75,35]
root = tree
#print("\nIterative inorder Traversal= ", end="")
#print(inorder_iterative(root))

def inorder_iterative2(root):
  result = ""
  if root == None:
    return

  stk = deque()

  while (len(stk) != 0 or root != None):
    #print('root',root)
    print('stack',len(stk))
    if root != None:
      stk.append(root)
      root = root.left
      continue

	# visit node
    result += str(stk[-1].key) + " "
    root = stk[-1].right
    stk.pop()
  #return str(result)
  return result


def bst_stack(root):
	result=""
	if root == None:
		return
	stk=deque()

	while len(stk) > 0 or root != None:
		if root != None:
			stk.append(root)
			root = root.left
			continue
		# visit node
		result += str(stk[-1].key) + " "
		root = stk[-1].right
		stk.pop()
	return result

# print(inorder_iterative2(root))
print(bst_stack(root))
