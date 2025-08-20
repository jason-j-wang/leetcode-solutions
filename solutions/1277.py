#https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-20
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix) 
        col = len(matrix[0])
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]:
                    dp[i + 1][j + 1] = (min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1)
                    ans += dp[i + 1][j + 1]
        return ans