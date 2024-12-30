class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [-1] * (1 + high)  
        mod = 10 ** 9 + 7        
        
        def solve(curr) :
            if curr > high : 
                return 0 
            if dp[curr] != -1 : 
                return dp[curr]
            dp[curr] = ((low <= curr <= high) + solve(curr + zero) + solve(curr + one)) % mod 
            return dp[curr]

        return solve(0)

assert(Solution().countGoodStrings(3, 3, 1, 1) == 8)
assert(Solution().countGoodStrings(2, 3, 1, 2) == 5)
print('yay')