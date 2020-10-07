import math
# Add any extra import statements you may need here




class Node:
  def __init__(self, x):
    self.data = x
    self.next = None


def remove_duplicates2(head):
  #TODO: Write - Your - Code
  #print(vars(head))
  hash={}
  node=head
  while node is not None:
    print(vars(node))
    if not node.data in hash:
      hash[node.data]=True
      print('new',node.data)
    node=node.next
  return head
  
def createLinkedList(arr):
  head = None
  tempHead = head
  for v in arr:
    if head == None:
      head = Node(v)
      tempHead = head
    else:
      head.next = Node(v)
      head = head.next
  return tempHead


def remove_duplicates(head):

  if head == None:
    return head

  dup_set = set()
  dup_set.add(head.data)
  curr = head

  while curr.next != None:
    if curr.next.data in dup_set:
      # Duplicate node found. Let's remove it from the list.
      curr.next = curr.next.next
    else:
      # Element not found in map, let's add it.
      dup_set.add(curr.next.data)
      curr = curr.next

  return head

def display(a):
	print(a)

test_case_number = 1

def check(expectedHead, outputHead):
  global test_case_number
  tempExpectedHead = expectedHead
  tempOutputHead = outputHead
  result = True
  while expectedHead != None and outputHead != None:
    result &= (expectedHead.data == outputHead.data)
    expectedHead = expectedHead.next
    outputHead = outputHead.next


  if not(outputHead == None and expectedHead == None):
    result = False


  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printLinkedList(tempExpectedHead)
    print(' Your output: ', end='')
    printLinkedList(tempOutputHead)
    print()
  test_case_number += 1


array1 = [4, 7, 4, 9, 7, 11, 4]
array1_expected = [4, 7, 9, 11]
list1 = createLinkedList(array1)
list1_expected = createLinkedList(array1_expected)
print("Original: ", end="")
display(list1)
list1 = remove_duplicates(list1)
print("After removing duplicates: ", end="")
display(list1)
check(list1, list1_expected)
