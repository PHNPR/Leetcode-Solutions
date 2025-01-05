class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(i in set(list(s)) for i in 'aeiou')