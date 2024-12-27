from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans, left = 0, values[0]

        for i in range(1, len(values)):
            ans = max(ans, left + values[i] - i)
            left = max(left, values[i] + i)
        
        return ans

check = lambda values, expectedAnswer : print(Solution().maxScoreSightseeingPair(values) == expectedAnswer)  

check([8, 1, 5, 2, 6], 11)
check([1, 2], 2)