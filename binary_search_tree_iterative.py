import collections

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
inorder(tree)
