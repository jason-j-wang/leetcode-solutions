#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/?envType=daily-question&envId=2025-12-28
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0
        ptr = n - 1

        for i in range(m):
            while grid[i][ptr] < 0 and ptr >= 0:
                ptr -= 1

            ans += n - ptr - 1
        return ans