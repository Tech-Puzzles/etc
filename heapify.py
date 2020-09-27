import random
# heapify tree of size n at subtree rooted at index i
#arr = [ 0 ] *100
arr = [ 0 ] *10
for i in range(len(arr)):
     #arr[i]=len(arr)-i
     arr[i]=i
random.shuffle(arr)
def buildheap(arr):
    for i in range(len(arr)):
        #arr=heapify(arr[0:i+1],i+1,i)    
        heapify(arr,i+1,i)    

def heapify(arr,n,i):
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

buildheap(arr)

