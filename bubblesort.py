from colorama import Fore, Back, Style
def visualize(i,j,arr):
	for ii in range(len(arr)):
		if ii==i:
			print(Back.BLUE + Style.BRIGHT ,end="")
		elif ii==j:
			print(Back.RED + Style.BRIGHT ,end="")
	
		print(arr[ii],end="")
		print(Style.RESET_ALL, end="")
	print()

def bubblesortX(arr):
	for i in range(len(arr)):
		for j in range(len(arr)):
		#for j in range(len(arr)-i):
			print(i,j,'test',arr[i],'<',arr[j],(arr[i]<arr[j]),'arr',arr)
			if arr[i] < arr[j]:
				t=arr[i]
				arr[i]=arr[j]
				arr[j]=t
	return arr

def bubblesort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
		#for j in range(len(arr)-i):
			print(j,j+1,'test',arr[j],'>',arr[j+1],(arr[j]>arr[j+1]),'arr',arr)
			visualize(j,j+1,arr)
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr

# print(bubblesort([1,2,3]))
# print(bubblesort([3,2,1]))
# print(bubblesort([9,1,3,2,1]))
print(bubblesort([9,8,7,6,5,4,3,2,1]))
#print(bubblesort([1,2,3,2,1]))
