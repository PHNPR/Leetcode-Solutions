from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        def bs(lo, hi, condition) :
            while lo < hi :
                mid = (lo + hi) // 2 
                if condition(mid) :
                    hi = mid 
                else :
                    lo = mid + 1
            return lo 
        
        i1 = bs(0, n, lambda x : nums[x] > 0) 
        i2 = bs(0, n, lambda x : nums[x] >= 0)

        return max(n - i1, i2)