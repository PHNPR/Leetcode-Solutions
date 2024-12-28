from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n, k2, k3 = len(nums), k << 1, k + (k << 1)
        s1, s2, s3 = map(sum, (nums[:k], nums[k:k2], nums[k2:k3]))
        m1, m12, m123 = s1, s1 + s2, s1 + s2 + s3 
        i1, i2, i3 = 0, 0, k 
        ans = [0, k, k2]

        for  i in range(1, n - k3 + 1) :
            s1 += nums[i + k - 1] - nums[i - 1]
            s2 += nums[i + k2 - 1] - nums[i + k - 1]
            s3 += nums[i + k3 - 1] - nums[i + k2 - 1]
            if s1 > m1 : m1, i1 = s1, i 
            if m1 + s2 > m12 : m12, i2, i3 = m1 + s2, i1, i + k  
            if m12 + s3 > m123 : m123, ans = m12 + s3, [i2, i3, i + k2]

        return ans  

check = lambda nums, k, expectedAnswer : print(Solution().maxSumOfThreeSubarrays(nums, k) == expectedAnswer)  

check([1,2,1,2,6,7,5,1], 2, [0, 3, 5])
check([1,2,1,2,1,2,1,2,1], 2, [0, 2, 4])