#https://leetcode.com/problems/largest-magic-square/description/?envType=daily-question&envId=2026-01-18
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_prefix = [[0 for _ in range(n)] for _ in range(m)]
        col_prefix = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            row_prefix[i][0] = grid[i][0]
            for j in range(1, n):
                row_prefix[i][j] = row_prefix[i][j-1] + grid[i][j]

        for j in range(n):
            col_prefix[0][j] = grid[0][j]
            for i in range(1, m):
                col_prefix[i][j] = col_prefix[i-1][j] + grid[i][j]

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row_prefix[i][j+k-1]
                    valid = True

                    if j > 0:
                        target -= row_prefix[i][j-1]

                    for x in range(i, i + k):
                        cur = row_prefix[x][j+k-1]

                        if j > 0:
                            cur -= row_prefix[x][j-1]

                        if cur != target:
                            valid = False
                            break
                    
                    if not valid:
                        continue

                    for y in range(j, j + k):
                        cur = col_prefix[i+k-1][y]

                        if i > 0:
                            cur -= col_prefix[i-1][y]

                        if cur != target:
                            valid = False
                            break
                    
                    if not valid:
                        continue

                    diag1 = 0
                    diag2 = 0

                    for d in range(k):
                        diag1 += grid[i+d][j+d]
                        diag2 += grid[i+d][j+k-d-1]
                    if diag1 == target and diag2 == target:
                        return k
            
        return 1

