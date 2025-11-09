#https://leetcode.com/problems/maximum-path-score-in-a-grid/description/
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # k is how much k we have left to use
        # dp[i][j][k] = max(dp[i+1][j][k - cost], dp[i][j+1][k - cost])
        ni = -float('inf')
        n = len(grid)
        m = len(grid[0])
        dp = {}

        def solve(i, j, cur_k):
            if i == n or j == m or cur_k < 0:
                return ni

            if (i, j, cur_k) in dp:
                return dp[(i, j, cur_k)]

            if i == n-1 and j == m - 1:
                dp[(i, j, cur_k)] = grid[i][j]
                return grid[i][j]

            score = ni
            if i + 1 < n:
                cost = 1 if grid[i+1][j] > 0 else 0
                if cost <= cur_k:
                    score = max(score, grid[i][j] + solve(i + 1, j, cur_k - cost))

            if j + 1 < m:
                cost = 1 if grid[i][j+1] > 0 else 0
                if cost <= cur_k:
                    score = max(score, grid[i][j] + solve(i, j + 1, cur_k - cost))
            
            dp[(i, j, cur_k)] = score
            return score

        solve(0, 0, k)
        return dp[(0, 0, k)] if dp[(0, 0, k)] != ni else -1