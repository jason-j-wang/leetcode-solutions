#https://leetcode.com/problems/sort-matrix-by-diagonals/description/
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        start_row = rows - 1
        start_col = 0
        should_reverse = True

        while start_row != 0 or start_col != cols:
            rows_left = rows -1 - start_row
            cols_left = cols -1 - start_col
            iterations = min(rows_left, cols_left) + 1
            arr = []
            for i, j in zip(range(iterations), range(iterations)):
                arr.append(grid[start_row+i][start_col+j])

            arr.sort(reverse=should_reverse)
            for i, j in zip(range(iterations), range(iterations)):
                grid[start_row+i][start_col+j] = arr[i]

            if start_row == 0 and start_col == 0:
                should_reverse = False
            
            if start_row != 0:
                start_row -= 1
            else:
                start_col += 1
        return grid