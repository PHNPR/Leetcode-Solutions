class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n, dic = len(s), {}
        x = n//k
        for i in range(0, n, x) :
            dic[s[i:i+x]] = dic.get(s[i:i+x], 0) + 1 
        for i in range(0, n, x) :
            if t[i:i+x] not in dic :
                return False 
            dic[t[i:i+x]] -= 1
            if dic[t[i:i+x]] == 0 :
                del dic[t[i:i+x]] 
        return True