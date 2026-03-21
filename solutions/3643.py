#https://leetcode.com/problems/flip-square-submatrix-vertically/description/?envType=daily-question&envId=2026-03-21
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range((k + 1) // 2):
            for j in range(y, y + k):
                grid[x+i][j], grid[x + k - 1 - i][j] = grid[x + k - 1 - i][j], grid[x+i][j]
        return grid