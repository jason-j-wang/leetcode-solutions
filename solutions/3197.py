#https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/description/?envType=daily-question&envId=2025-08-23
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rotated_grid = self.rotate(grid)
        return min(self.solve(grid), self.solve(rotated_grid))

    def rotate(self, grid):
        n = len(grid)
        m = len(grid[0])

        rotated = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            for j in range(m):
                rotated[m - j - 1][i] = grid[i][j]

        return rotated
        
    def minArea(self, grid, t, b, l, r):
        right = 0
        left = float("inf")
        top = float("inf")
        bot = 0


        for i in range(t, b + 1):
            for j in range(l, r + 1):
                if grid[i][j]:
                    right = max(right, j)
                    left = min(left, j)
                    top = min(top, i)
                    bot = max(bot, i)

        return (right - left + 1) * (bot - top +1)

    def solve(self, grid):
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        ans = n * m

        for i in range(n - 1):
            for j in range(m - 1):
                ans = min(ans, self.minArea(grid, 0, i, 0, m - 1)
                 + self.minArea(grid, i + 1, n - 1, 0, j)
                 + self.minArea(grid, i + 1, n - 1, j + 1, m - 1))

                ans = min(ans, self.minArea(grid, 0, i, 0, j)
                    + self.minArea(grid, 0, i, j + 1, m - 1)
                    + self.minArea(grid, i + 1, n - 1, 0, m - 1))


        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                ans = min(ans, self.minArea(grid, 0, i, 0, m - 1)
                    + self.minArea(grid, i + 1, j, 0, m - 1)
                    + self.minArea(grid, j + 1, n - 1, 0, m - 1))
        
        return ans