from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        t, n, mod = len(target), len(words[0]), int(1e9) + 7
        arr = [{} for _ in range(n)]
        dp = [[-1 for _ in range(n)] for _ in range(t)]

        for j in range(n) :
            for word in words :
                if word[j] not in arr[j] :
                    arr[j][word[j]] = 0 
                arr[j][word[j]] += 1 
        
        def solve(i, j) :
            if i == t : return 1 
            if j == n : return 0
            if dp[i][j] != -1 : return dp[i][j]
            val = solve(i, j + 1)
            if target[i] in arr[j] :
                val += solve(i + 1, j + 1) * arr[j][target[i]]
            dp[i][j] = val % mod 
            return dp[i][j]
        
        return solve(0, 0)

assert(Solution().numWays(["acca","bbbb","caca"], "aba") == 6)
assert(Solution().numWays(["abba","baab"], "bab") == 5)
print('yay')