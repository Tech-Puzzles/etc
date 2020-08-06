from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        map={}
        count=0
        pairs=set()
        #nums=set(nums)
        #print('set',nums)
        for i in nums:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
            #map[i]=True
        for i in nums:
            if k == 0:
                if map[i] > 1:
                    #print(i,'+',k,'in',map)
                    #count+=1
                    pairs.add((i,i+k))
            else:
                if i+k in map:
                    #print(i,'+',k,'in',map)
                    #count+=1
                    pairs.add((i,i+k))
                elif i-k in map:
                    #print(i,'-',k,'in',map)
                    pairs.add((i-k,i))
                    #count+=1
        #return count
        #print(pairs)
        return len(pairs)
            
        

test=Solution()
print(test.findPairs([1,2,3,4],1))
