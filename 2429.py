class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt = bin(num2).count('1')
        ans = i = 0 
        for i in range(31, -1, -1) :
            if cnt and (num1 & (1 << i)) :
                ans |= (1 << i)
                cnt -= 1 
        while cnt :
            if not ans & (1 << i) :
                ans |= (1 << i)
                cnt -= 1 
            i += 1 
        return ans 