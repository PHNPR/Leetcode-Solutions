from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        vis, n, ans = set(), len(A), []
        for i in range(n) :
            vis.add(A[i])
            vis.add(B[i])
            ans.append(2 * (i + 1) - len(vis))
        return ans 