#https://leetcode.com/problems/set-matrix-zeroes/description/?envType=daily-question&envId=2025-05-21
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_col = False
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            if matrix[row][0] == 0:
                first_col = True
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, 0, -1):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
            if first_col:
                matrix[row][0] = 0