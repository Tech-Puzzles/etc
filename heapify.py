import random
# heapify tree of size n at subtree rooted at index i
arr = [ 0 ] *100
#arr = [ 0 ] *10
for i in range(len(arr)):
     #arr[i]=len(arr)-i
     arr[i]=i
random.shuffle(arr)
def buildheap(arr):
    for i in range(len(arr)):
        #arr=heapify(arr[0:i+1],i+1,i)    
        heapify(arr,i+1,0)    

def build_max_heap(array):
    for i in reversed(range(len(arr)//2)):
        #min_heapify(array, i)
        print('heapify2',i,len(arr))
        heapify2(arr, len(arr), i)

def heapify2(arr,n,i):
    print(arr[0:n],n,i)
    largest=i
    l=2*i+1
    r=2*i+2
    print('root',i,'l',l,'n',n)
    if l < n and arr[l] > arr[largest]:
        largest=l
    if r < n and arr[r] > arr[largest]:
        largest=r

    if largest != i: 
        print('swap')
        arr[i],arr[largest]= arr[largest],arr[i]
        heapify(arr,n,i)
        
    #return arr

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i, swapitem=None): 
    print('heapify',arr,'size of heap: n',n,'subtree rooted at i',i);
    #visualize(arr,swapitem)
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
    print('lookat','left',l,'parent',i,l//2,'right',r);

    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 

    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 

    # Change root, if needed 
    if largest != i: 
        print('swap')
        #time.sleep(1)
        arr[i],arr[largest] = arr[largest],arr[i] # swap 

        # Heapify the root. 
        heapify(arr, n, largest, i) 
    #time.sleep(1)




def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)

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

# buildheap(arr)
build_max_heap(arr)
print('isHeap',isHeap(arr,len(arr),0))
