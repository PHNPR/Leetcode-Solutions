from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(val) :
            return nums[val] >= target 
        
        lo, hi = 0, len(nums) - 1 

        while lo < hi :
            mid = (lo + hi) // 2 
            if condition(mid) :
                hi = mid 
            else :
                lo = mid + 1 

        return lo if nums[lo] == target else -1     