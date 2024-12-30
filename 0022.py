from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def solve(i, j) :
            if i == 0 and j == 0 :
                return ['']
            ans = []
            if i :
                ans.extend(['(' + suff for suff in solve(i - 1, j)])
            if i < j :
                ans.extend([')' + suff for suff in solve(i, j - 1)])
            return ans 
        
        return solve(n, n)