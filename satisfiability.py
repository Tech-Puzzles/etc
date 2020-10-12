def two_to_the_n(n):
    if n == 0:
        print()
        return
    print('T',end="")
    print('F',end="")
    for i in range(n):
        two_to_the_n(n-1)

# two_to_the_n(3)

def bool_combs(n):
    print('call',n)
    if not n:
        return [[]]
    result = []
    for comb in bool_combs(n-1):
        print('comb',comb)
        result.append(comb + [True])
        result.append(comb + [False])
    return result

# print(bool_combs(1))
set1=bool_combs(10)
print(len(set1))



