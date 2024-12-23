from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)) :
            if target - nums[i] in dic :
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i 

check = lambda nums, target, expectedAnswer : Solution().twoSum(nums, target) == expectedAnswer  

print(check([2, 7, 11, 15], 9, [0, 1]))
print(check([3, 2, 4], 6, [1, 2]))
print(check([3, 3], 6, [0, 1]))