from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n, s, pre, cnt = len(nums), sum(nums), 0, 0 

        for i in range(n - 1) :
            pre += (nums[i] << 1)
            cnt += (pre >= s)
        
        return cnt 