import time
import random
from colorama import Fore, Back, Style
def visualize(arr,swapitem=None):
    #print('\x1b[2J')
    print('swapitem',swapitem)
    print(arr)
    if swapitem is not None:
        print('swapitem',swapitem)
        print(Back.RED + Style.BRIGHT  ,end="")
        print(">"*swapitem,end="")
        print(Back.RED + Style.BRIGHT +"S" ,end="")
        print(Style.RESET_ALL, end="")
        print()
        #time.sleep(1)
    for ii in range(len(arr)):
        print(" "*arr[ii],end="")
        print(Back.BLUE + Style.BRIGHT +"x" ,end="")
        print(Style.RESET_ALL, end="")
        print()
#         for jj in range(len(arr)):
#             if jj==arr[ii]:
#                 print(Back.BLUE + Style.BRIGHT +"x" ,end="")
#                 print(Style.RESET_ALL, end="")
#                 print()
#             else:
#                 print(" " ,end="")
    
    print()
    #time.sleep(.5)
# Python program for implementation of heap Sort 

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i, swapitem=None): 
    print('heapify',arr,'size of heap: n',n,'subtree rooted at i',i);
    visualize(arr,swapitem)
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

# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 

    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        print('calling',i)
        heapify(arr, n, i) 

    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        print('calling sort',i)
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
        #visualize(arr)

# Driver code to test above 
# arr = [ 12, 11, 13, 5, 6, 7] 
#arr = [ 0 ] *100
arr = [ 0 ] *10
for i in range(len(arr)):
     #arr[i]=len(arr)-i
     arr[i]=i
#random.shuffle(arr)
arr=[4,3,5]
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
#for i in range(n): 
    #print ("%d" %arr[i]), 
# This code is contributed by Mohit Kumra 

