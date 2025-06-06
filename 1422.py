class Solution:
    def maxScore(self, s: str) -> int:
        n, l, r, ans = len(s), 0, s.count('1'), 0

        for i in range(n - 1) :
            if s[i] == '0' :
                l += 1 
            else :
                r -= 1 
            ans = max(ans, l + r)

        return ans