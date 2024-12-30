from typing import List
from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, q, n = [], deque(), len(nums)

        for i in range(n) :
            while q and nums[i] >= nums[q[-1]] :
                q.pop()
            while q and q[0] + k <= i :
                q.popleft()
            q.append(i)
            if i >= k -1 :
                ans.append(nums[q[0]])
        
        return ans