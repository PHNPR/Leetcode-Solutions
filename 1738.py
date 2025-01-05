from typing import List
import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        (m, n), heap = map(len, (matrix, matrix[0])), []
        heapq.heapify(heap)

        for i in range(m) :
            for j in range(n) :
                if i and j :
                    matrix[i][j] ^= matrix[i-1][j] ^ matrix[i][j-1] ^ matrix[i-1][j-1]
                elif i :
                    matrix[i][0] ^= matrix[i-1][0]
                elif j :
                    matrix[0][j] ^= matrix[0][j-1]
                if len(heap) == k :
                    heapq.heappushpop(heap, matrix[i][j])
                else :
                    heapq.heappush(heap, matrix[i][j])

        return heap[0]