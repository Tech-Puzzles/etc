import random

def isHeap(arr, i, n): 
      
# If a leaf node  
    if i > int((n - 2) / 2):  
        return True
      
    # If an internal node and is greater  
    # than its children, and same is 
    # recursively true for the children  
    if(arr[i] >= arr[2 * i + 1] and 
       arr[i] >= arr[2 * i + 2] and 
       isHeap(arr, 2 * i + 1, n) and
       isHeap(arr, 2 * i + 2, n)): 
        return True
      
    return False


def heapify(arr,i,n):
    largest=i
    left=i*2+1
    right=i*2+2
    if left < n and arr[left] > arr[largest]:
        largest=left
    if right < n and arr[right] > arr[largest]:
        largest=right
    if largest != i:
        #swap
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,largest,n)


#arr=[1,2,3,4]
#arr=[1,2,3,4]
# arr=[1,2,3,4,5,6,7]
arr=[0]*10
for i in range(len(arr)):
    arr[i]=i
random.shuffle(arr)
arr = [ 1, 3, 5, 4, 6, 13,  10, 9, 8, 15, 17 ]

def heapsort(arr):
        for i in reversed(range(len(arr)//2)):
            heapify(arr,i,len(arr))
"""
        for i in reversed(range(len(arr))):
            arr[0],arr[i] = arr[i],arr[0]
            heapify(arr,0,i)
"""

    #    print(arr)

heapsort(arr)

def heapinsert(arr,i):
    # bubble up

    parent=(i-1)//2
    while i != 0:
        if arr[parent] < arr[i]:
            arr[parent] , arr[i] = arr[i] , arr[parent] 
            i=parent
            parent=(i-1)//2
            
        
print('isHeap',isHeap(arr,len(arr),0))
print(arr)

arr.append(100)
heapinsert(arr,len(arr)-1)
print(arr)

print('isHeap',isHeap(arr,len(arr),0))
