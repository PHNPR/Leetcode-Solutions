class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0 
        for i in range(97, 123) :
            try :
                l, r = s.index(chr(i)), s.rindex(chr(i))
                ans += len(set(s[l+1:r]))
            except :
                continue 
        return ans
