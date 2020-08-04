""" 
class MedianFinder:

    def __init__(self):

        

    def addNum(self, num: int) -> None:
        

    def findMedian(self) -> float:
"""
       


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []#max heap
        self.hi = []#min heap

    def addNum(self, num: int) -> None:
        """
        :type num: int
        :rtype: None
        """
        if not self.lo: # push the value to the max heap by default
            heappush(self.lo,-num)
        elif num<-self.lo[0]:
            heappush(self.lo,-num)
            if len(self.lo)>len(self.hi)+1:
                heappush(self.hi,-heappop(self.lo))
        else:
            heappush(self.hi,num)
            if len(self.hi)>len(self.lo):
                heappush(self.lo,-heappop(self.hi))
                
    def findMedian(self) -> float:
        """
        :rtype: float
        """
        if len(self.lo)>len(self.hi):
            return -self.lo[0]
        else:
            return (-self.lo[0]+self.hi[0])*0.5


test=MedianFinder()
test.addNum(5)
print(test.findMedian())
test.addNum(10)
print(test.findMedian())
