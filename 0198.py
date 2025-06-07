from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = 0

        for num in nums :
            a, b = max(a, b), max(b, a + num)
        
        return max(a, b)