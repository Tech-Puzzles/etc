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

def heapsort(arr):
    for i in reversed(range(len(arr)//2)):
        #print('i',i)
        heapify(arr,i,len(arr))
    print('heapify',arr)
    for i in range(len(arr)-1):
        print('calling sort',len(arr)-i-1)
        #swap 0 and i
        arr[0],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[0]
        heapify(arr,0,len(arr)-i-1)


heapsort(arr)
print(arr)

