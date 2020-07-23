from typing import List

class Solution:
    def LongestFibSubseq(self,A):  
      
        # Store all array elements in  
        # a hash table  
        print(A)
        print(type(A))
        print(set)
        S = set(A)  
        n=len(A)
        maxLen = 0
      
        for i in range(0, n):  
                for j in range(i + 1, n):  
              
                    x = A[j]  
                    y = A[i] + A[j]  
                    length = 2
              
                    # check until next fib  
                    # element is found  
                    while y in S:  
              
                            # next element of fib subseq  
                            z = x + y  
                            x = y  
                            print('found',y,'=',A[i],'+',A[j],length+1)
                            y = z 
                            length += 1
                    maxLen = max(maxLen, length)  
                      
        return maxLen if maxLen >= 3 else 0

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        print('===>',A)
        S = set(A)
        answers={}
        if len(A)<3:
            return 0
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                #print(i,j,A[i],A[j])
                length=2
                x = A[j]
                y = A[i]+A[j]
                while y in S:
                    length+=1
                    print('found',y,'=',A[i],'+',A[j],length)
                    z=y
                    y=x+y
                    x=z
                #print('(',i,',',j,')',length)
                answers[(i,j)]=length
        #print(answers)
        return(max(answers.values()))
    
    
test=Solution()
print(test.lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50]))
print(test.LongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50]))
        


