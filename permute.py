def permute(A):
    print('process',A)
    if len(A) == 1:
        return A
    #else:
        #permute(A[0:-2])
        #permute(A[-1])

    res = []
    for permutation in permute(A[1:]):
        for i in range(len(A)):
            print('append', permutation[:i] ,'+', A[0:1] , '+', permutation[i:])
            res.append(permutation[:i] + A[0:1] + permutation[i:])
    return res

# print(permute([1,2]))
print(permute('AB'))
print(permute('ABC'))
