#https://leetcode.com/problems/equal-sum-grid-partition-i/description/?envType=daily-question&envId=2026-03-25
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        row_sum = [0 for _ in range(rows)]
        col_sum = [0 for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                num = grid[i][j]
                row_sum[i] +=  num
                col_sum[j] += num


        total_row = sum(row_sum)
        total_col = sum(col_sum)

        cur = 0
        for i in range(rows):
            cur += row_sum[i]
            total_row -= row_sum[i]
            if cur == total_row:
                return True

        cur = 0
        for i in range(cols):
            cur += col_sum[i]
            total_col -= col_sum[i]
            if cur == total_col:
                return True
        return False
