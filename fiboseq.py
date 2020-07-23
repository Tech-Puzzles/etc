from typing import List
from colorama import Fore, Back, Style
import time

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        operations=0
        print('===>',A)
        answers={}
        if len(A)<3:
            return 0
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                #print(i,j,A[i],A[j])
                length=2
                location=1
                trail=i
                lead=j
                operations+=1
                while j+location < len(A):
                    print('\x1b[2J')
                    print('input',A)
                    print('testing',A[trail],'+',A[lead],'=',A[j+location],A[trail]+A[lead]==A[j+location])
                    print('operations',operations)
                    # time.sleep(1)
                    if A[trail]+A[lead]==A[j+location]:
                        length+=1
                        trail=lead
                        lead=trail+1
                    #lead+=1
                    operations+=1
                    location+=1
                print('(',i,',',j,')',length)    
                answers[(i,j)]=length
        #print(answers)
        return(max(answers.values()),operations)
    
    
test=Solution()
print('answer:', test.lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50]))
        


