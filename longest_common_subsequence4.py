def lcs(X,Y):
    m=len(X)
    n=len(Y)

    L=[]
    for _ in range(m+1):
        L.append([0]*(n+1))

    #print(L)
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                pass
            elif X[i-1] == Y[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    print("",end="      ")
    for item in Y:
        print(item,end="  ")
    print()
    i=0
    for item in L:
        #if i >= len(X):
        #    break
        if i==0:
            print(" ",item)
        else:
            print(X[i-1],item)
        #print(i,item)
        i+=1
    return L[m][n]


#X="XABXABXAB"
#Y="XAB"
# X=  "Mary had a little lamb"
# Y= "Mary little"
X="It is a Mury had a little lamb"
Y="It is a Mary had a little lamb"
print('len(X)',len(X))
print('len(Y)',len(Y))
print(lcs(X,Y))
        
