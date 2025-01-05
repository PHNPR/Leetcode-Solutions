from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        
        for i, j in requests :
            dp[i] += 1 
            dp[j + 1] -= 1 
        
        for i in range(1, n + 1) :
            dp[i] += dp[i - 1]

        dp = sorted([i for i in dp if i], reverse = True)
        nums.sort(reverse = True)

        return sum((nums[i] * dp[i] for i in range(len(dp)))) % (10 ** 9 + 7)