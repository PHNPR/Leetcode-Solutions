from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        posvals = {0 : 1}
        for num in nums :
            new = {}
            for curr in posvals :
                new[curr + num] = new.get(curr + num, 0) + posvals[curr] 
                new[curr - num] = new.get(curr - num, 0) + posvals[curr] 
            posvals = new
        return posvals.get(target, 0)

check = lambda nums, target, expectedAnswer : print(Solution().findTargetSumWays(nums, target) == expectedAnswer)  

check([1,1,1,1,1], 3, 5)
check([1], 1, 1)