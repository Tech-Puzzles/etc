from collections import deque
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

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

tree=None
tree=insert(tree,10)
tree=insert(tree,20)

def inorder_iterative(root):
    result = ""
    stk=deque()

    while len(stk) > 0 or root != None:
        if root != None:
            stk.append(root)
            # visit left
            root = root.left
            continue
        # visit node
        # visit right
        top = stk[-1]
        result += str(top.key) + " " 
        root=top.right
        stk.pop()
    return result

print(inorder_iterative(tree))
