from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)) :
            if target - nums[i] in dic :
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i 

assert(Solution().twoSum([2, 7, 11, 15], 9) == [0, 1])
assert(Solution().twoSum([3, 2, 4], 6) == [1, 2])
assert(Solution().twoSum([3, 3], 6) == [0, 1])