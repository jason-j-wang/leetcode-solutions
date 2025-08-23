#https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/submissions/1744019532/?envType=daily-question&envId=2025-08-23
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        right = 0
        left = float("inf")
        top = float("inf")
        bot = 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    right = max(right, j)
                    left = min(left, j)
                    top = min(top, i)
                    bot = max(bot, i)

        return (right - left + 1) * (bot - top +1)