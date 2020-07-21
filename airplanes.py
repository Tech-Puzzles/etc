"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        max1=0
        sum=0
        order=[]
        linedict={}
        for item1 in airplanes:
            #print(item)
            #item=(item1.start,item1.end)
            item=item1
            if item[0] in linedict:
                linedict[item[0]]+=1
            else:
                linedict[item[0]]=1
            if item[1] in linedict:
                linedict[item[1]]-=1
            else:
                linedict[item[1]]=-1
        #print(linedict)                
        order=sorted(linedict.keys())
        #print(order)
        for item in order:
            #print(item,'BEFORE',max1,linedict[item])
            sum+=linedict[item]
            max1 = max(sum, max1)
            #print(item,'AFTER',max1,linedict[item])
        return max1
test=Solution()
print(test.countOfAirplanes([(1,2),(3,4)]))
print(test.countOfAirplanes([(9,10),(1,4),(3,4),(11,12),(1,13)]))
