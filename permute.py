def permute(A):
    print('calling,process',A)
    if len(A) == 1:
        print('returning',A)
        return A
    #else:
        #permute(A[0:-2])
        #permute(A[-1])
    print('setting result to empty')
    res = []
    for permutation in permute(A[1:]):
         print('step1',permutation)
         for i in range(len(A)):
             print('append', permutation[:i] ,'+', A[0:1] , '+', permutation[i:])
             #res.append(permutation[:i] + A[0:1] + permutation[i:])
             res.append(permutation[:i] + A[0] + permutation[i:])
#     for permutation in permute(A[0:-2]):
#         print('step1',permutation)
#         for i in range(len(A)):
#             print('append', permutation[:i] ,'+', A[-2:-1] , '+', permutation[i:])
#             res.append(permutation[:i] + A[-2:-1] + permutation[i:])
    print('returning',res)
    return res

# print(permute([1,2]))
# print(permute('AB'))
# print(permute('ABC'))
# print(permute('ABC'*10))


def permutations(string_input, array, fixed_value=""):
    print('calling',string_input)
    for ch in string_input:
        permutations(string_input.replace(ch, ""), array, fixed_value + ch)
    if not string_input:
        array.append(fixed_value)

array = []
# permutations("cat", array)
# print(array)

def permutelist(A,list,rest=[]):
    print('calling',A)
    if len(A)==1:
        return A
    for i in A:
        permutelist(A[i:],list,A[:i])
    if len(A)==0:
        list.append(rest)

    
list = []
# permutelist([1,2,3], list)
# print(list)


def permutex(a, l, r):
    if l==r:
        print(a)
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permutex(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
A=[1,2,3]
permutex(A, 0, len(A)-1)
