from typing import List

class Solution:
    def maxRunTime(self, n: int, arr: List[int]) -> int:
        
        def condition(t) :
            return sum(min(t, i) for i in arr) < n * t
        
        lo, hi = 0, 1 + sum(arr) // n 

        while lo < hi :
            mid = (lo + hi) // 2 
            if condition(mid) :
                hi = mid 
            else :
                lo = mid + 1 
        
        return lo - 1 