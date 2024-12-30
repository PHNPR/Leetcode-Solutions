from typing import List 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        rite = [n] * n
        left = [-1] * n
    
        stack = [0]
        for i in range(1, n) :
            while stack and heights[i] < heights[stack[-1]] :
                rite[stack.pop()] = i 
            stack.append(i)
    
        stack = [n - 1]
        for i in range(n - 2, -1, -1) :
            while stack and heights[i] < heights[stack[-1]] :
                left[stack.pop()] = i 
            stack.append(i)
        
        return max((rite[i] - left[i] - 1) * heights[i] for i in range(n)) 