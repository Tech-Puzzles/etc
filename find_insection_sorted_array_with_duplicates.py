def find_insection_sorted_array_with_duplicates_inner(ar1,ar2):
	m=len(ar1)
	n=len(ar2)
	i,j=0,0
	intersection=[]
	while i < m and j < n:
		if ar1[i] == ar2[j]:
			#print(ar1[i],end=",")
			intersection.append(ar1[i])
			i+=1
			j+=1
		elif ar1[i] < ar2[j]:
			i+=1
		else:
			j+=1

	return intersection	

def find_insection_sorted_array_with_duplicates(ar1,ar2):
	m=len(ar1)
	n=len(ar2)

	if m < n:
		return find_insection_sorted_array_with_duplicates_inner(ar1,ar2)
	else:
		return find_insection_sorted_array_with_duplicates_inner(ar2,ar1)

print(find_insection_sorted_array_with_duplicates([1,5,5,9],[5,5]))
print(find_insection_sorted_array_with_duplicates([1,5,5,9,11],[5,5,11]))

print(
find_insection_sorted_array_with_duplicates(
find_insection_sorted_array_with_duplicates([1,5,5,9,11],[5,5,11]),[5,6]))
