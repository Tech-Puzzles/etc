def countingsort(arr):
    # arr from 0 to k
    k=max(arr)
    sortarray=[0]*(k+1)
    for i in range(len(arr)):
        #print('setting',arr[i])
        sortarray[arr[i]]+=1
    print(sortarray)


    """
    lists={}
    # set up spare
    for i in len(arr):
        lists[i]=[]
    for i in arr:
    """

# countingsort([9,7,6,5,9,9])
countingsort([9,7,6,5,9,9,1000])
