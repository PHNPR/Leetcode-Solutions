from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, end  = 0, -1
        n = len(nums)

        while k and end < n - 1 :
            end += 1 
            if not nums[end] :
                k -= 1 

        ans = end - start + 1 

        while end < n - 1 :
            end += 1 
            if not nums[end] :
                while nums[start] :
                    start += 1 
                start += 1 
            ans = max(ans, end - start + 1)

        return ans                 