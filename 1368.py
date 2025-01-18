from typing import List
import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        heap = [(0, 0, 0)] #(cost, x, y)
        m, n = map(len, (grid, grid[0]))
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0 
        dirs = (0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)

        while heap :
            cost, x, y = heapq.heappop(heap)
            if x == m - 1 and y == n - 1 :
                return cost 
            if cost > dp[x][y] :
                continue 
            for dx, dy, sgn in dirs :
                if 0 <= x + dx < m and 0 <= y + dy < n :
                    dcost = int(grid[x][y] != sgn)
                    if dp[x + dx][y + dy] > cost + dcost :
                        dp[x + dx][y + dy] = cost + dcost 
                        heapq.heappush(heap, (cost + dcost, x + dx, y + dy))