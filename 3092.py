from typing import List 
import heapq 

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        dic, heap = {}, []
        heapq.heapify(heap)
        ans = []

        for ni, fi in zip(nums, freq) :
            dic[ni] = dic.get(ni, 0) + fi
            heapq.heappush(heap, (-dic[ni], ni)) 

            while dic[heap[0][1]] != -heap[0][0] :
                heapq.heappop(heap)
            
            ans.append(-heap[0][0])
        
        return ans 

assert(Solution().mostFrequentIDs([2,3,2,1], [3,2,-3,1]) == [3,3,2,2])
assert(Solution().mostFrequentIDs([5,5,3], [2,-2,1]) == [2,0,1])
print('yay')