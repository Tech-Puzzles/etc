import random
def heapify(arr,i,n):
    largest=i
    left=largest*2+1
    right=largest*2+2
    #print('right',right,'n',n)
    #print('arr:right',arr[right],'arr:largest',arr[largest])
    if left<n and arr[left] > arr[largest]:
        largest=left
    if right<n and arr[right] > arr[largest]:
        largest=right
    #print('i != largest',i,largest)
    if i != largest:
        # root is not largest
        # swap
        print('swap',arr[i],arr[largest])
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,largest,n)


arr=[4,3,5]
arr=[0]*100
for i in range(len(arr)):
	arr[i]=i
random.shuffle(arr)

def heapsort(arr):
    for i in reversed(range(len(arr)//2)):
        #print('i',i)
        heapify(arr,i,len(arr))
    print('heapify',arr)
    #for i in range(len(arr)-1):
    for i in range(len(arr)-1):
        end=len(arr)-i-1
        print('calling sort',len(arr)-i-1)
        #swap 0 and end
        #arr[0],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[0]
        #heapify(arr,0,len(arr)-i-1)
        arr[0],arr[end] = arr[end],arr[0]
        heapify(arr,0,end)

arr=[1,2,3,4,5]

heapsort(arr)
print(arr)

