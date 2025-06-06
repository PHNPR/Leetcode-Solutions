from typing import List 

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        dp = [0] * (len(s) + 1)
        
        for a , b , c in shifts :
            dp[a] += (2*c - 1) 
            dp[b + 1] -= (2*c - 1)
        
        f = lambda i : chr(97 + (ord(s[i]) - 97 + dp[i]) % 26)
        val = f(0)

        for i in range(1, len(s)) :
            dp[i] += dp[i - 1]
            val += f(i)
        
        return val