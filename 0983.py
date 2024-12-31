from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp, j = [0] * (days[-1] + 1), 0
        
        for day in range(1, days[-1] + 1):
            if day != days[j] :
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[day - 1] + costs[0], 
                    dp[max(0, day - 7)] + costs[1], 
                    dp[max(0, day - 30)] + costs[2]
                )
                j += 1 

        return dp[-1]