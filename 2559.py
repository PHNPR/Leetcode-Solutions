from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        dp, v = [0], set(['a', 'e', 'i', 'o', 'u'])
        for word in words  :
            dp.append(dp[-1] + int(word[0] in v and word[-1] in v))
        return [dp[r + 1] - dp[l] for l, r in queries]