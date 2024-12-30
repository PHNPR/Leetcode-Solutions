from typing import List 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0 : return []
        
        dic = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl', 
            '6' : 'mno',
            '7' : 'pqrs', 
            '8' : 'tuv', 
            '9' : 'wxyz'
        }
        
        def backtrack(idx) :
            if idx == n :
                return ['']
            ans = []
            for letter in dic[digits[idx]] :
                ans.extend([letter + suff for suff in backtrack(idx + 1)])
            return ans 
        
        return backtrack(0)