#https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/?envType=daily-question&envId=2025-03-28
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ans = [-1 for i in range(len(queries))]
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        mapped = [(queries[i], i) for i in range(len(queries))]
        mapped.sort()
        
        queue = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        score = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        for q in range(len(queries)):
            query, i = mapped[q]

            while queue:
                value, r, c = queue[0]

                if value >= query:
                    ans[i] = score
                    break

                heapq.heappop(queue)
                
                score += 1

                for row, col in dirs:
                    if r + row >= 0 and r + row < m and c + col >= 0 and c + col < n and not visited[r+row][c+col]:
                        heapq.heappush(queue, (grid[r+row][c+col], r+row, c+col))
                        visited[r+row][c+col] = True

            if ans[i] == -1:
                ans[i] = score
        return ans


