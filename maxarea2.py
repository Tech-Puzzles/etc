"""
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        
        if(n == 0)
            return 0;
        
        vector<int> left_min(n, -1);
        vector<int> right_min(n, n);
        stack<int> stk;
        
        // calculate right min boundary for every bar. TC:O(n)
        for(int i = 0;i<n;++i) {
            while(stk.size() && heights[stk.top()] > heights[i]) {
                right_min[stk.top()] = i;
                stk.pop();
            }
            stk.push(i);
        }
        
        //pop remaining elements for which boundry is not found
        // default boundary right boundary is set to n
        while(stk.size())
            stk.pop();
        
        // calculate left min boundary for every bar. TC:O(n) 
        for(int i = n-1;i>=0;--i) {
            while(stk.size() && heights[stk.top()] > heights[i]) {
                left_min[stk.top()] = i;
                stk.pop();
            }
            stk.push(i);
        }
        //remaining elements for which boundry is not found
        // default boundary left boundary is set to -1
            
       
        int area = -1;
       
        //calculate area based on left and right min boundaries. TC:O(n)
        for(int i = 0;i<n;++i) {
            //right_min[i] - left_min[i] - 1 --> this number of bars
            //excluding last and first
            area = max(area, heights[i]*(right_min[i] - left_min[i] - 1));
        }
        
        return area;
        
    }
};
"""
from typing import List
from collections import deque
def top(stk):
	if len(stk):
		return stk[-1]
	else:
		return None

class Solution:
    def largestRectangleArea(self,heights: List[int]) -> int:
        print('input',heights)
        n = len(heights)
        
        if n == 0:
            return 0
        
        # vector<int> left_min(n, -1);
        left_min = [-1]*n
        # vector<int> right_min(n, n);
        right_min = [n]*n
        # stack<int> stk;
        # stk = []
        stk = deque()
        
        # calculate right min boundary for every bar. TC:O(n)
        for i in range(n):
            while len(stk) and heights[top(stk)] > heights[i]:
                right_min[top(stk)]=i
                stk.pop()
            # stk.push(i)
            stk.append(i)
        print('right_min',right_min)

        while len(stk):
            stk.pop()

        print('stack',stk)

        return
"""
        for(int i = 0;i<n;++i) {
            while(stk.size() && heights[stk.top()] > heights[i]) {
                right_min[stk.top()] = i;
                stk.pop();
            }
            stk.push(i);
        }
"""

        
"""
        //pop remaining elements for which boundry is not found
        // default boundary right boundary is set to n
        while(stk.size())
            stk.pop();
        
        // calculate left min boundary for every bar. TC:O(n) 
        for(int i = n-1;i>=0;--i) {
            while(stk.size() && heights[stk.top()] > heights[i]) {
                left_min[stk.top()] = i;
                stk.pop();
            }
            stk.push(i);
        }
        //remaining elements for which boundry is not found
        // default boundary left boundary is set to -1
            
       
        int area = -1;
       
        //calculate area based on left and right min boundaries. TC:O(n)
        for(int i = 0;i<n;++i) {
            //right_min[i] - left_min[i] - 1 --> this number of bars
            //excluding last and first
            area = max(area, heights[i]*(right_min[i] - left_min[i] - 1));
        }
        
        return area;
        
    }
};
"""

test=Solution()
print(test.largestRectangleArea([6,2,4,5,4,3,1]))
