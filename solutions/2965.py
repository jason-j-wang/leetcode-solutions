#https://leetcode.com/problems/find-missing-and-repeated-values/description/?envType=daily-question&envId=2025-03-06
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        a = 0
        b = ((n ** 2) * (n ** 2 + 1)) // 2

        for i in range(n):
            for j in range(n):
                if grid[i][j] in seen:
                    a= grid[i][j]
                b -= grid[i][j]


        return [a, b + a]