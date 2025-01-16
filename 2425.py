from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        (n1, n2), ans = map(len, (nums1, nums2)), 0
        if n1 % 2 :
            for i in nums2 :
                ans ^= i 
        if n2 % 2 :
            for i in nums1 :
                ans ^= i 
        return ans 