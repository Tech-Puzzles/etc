class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
        
    def __str__(self):
        curr=self
        if curr is None:
            return ""
        str1=[str(curr.data)]
        while curr.next is not None:
            curr=curr.next
            str1.append('curr.data: %s'%curr.data)
        return "\n".join(str1)

def remove_duplicates(head):
    if head is None:
        return head
    curr=head
    hash={}
    # while curr is not None and curr.next is not None:
    while curr.next is not None:
        if curr.next.data in hash:
            # skip
            curr.next=curr.next.next
        else:
            hash[curr.data]=True
            curr=curr.next
    return head

a=Node(1)
b=a.next=Node(1)
c=b.next=Node(3)

# print(Node(1))
print(a)

print(remove_duplicates(a))

