#https://leetcode.com/problems/ones-and-zeroes/?envType=daily-question&envId=2025-11-11
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][m][n] => the max subset size possible up to strs at idx i (including i) with m and n remaining
        # d[i][m][n] =
        #   if valid: max(dp[i+1][m][n], dp[i+1][m-mi][n-ni])
        #   if not valid: dp[i+1][m][n]

        memo = [[[-1 for _ in range(n+1)] for _ in range(m + 1)] for _ in range(len(strs))]
        counts = [None for _ in range(len(strs))]

        for i, bin_string in enumerate(strs):
            counts[i] = (bin_string.count('0'), bin_string.count('1'))

        return self.solve(strs, m, n, 0, memo, counts)


    def solve(self, strs, m, n, idx, memo, counts):
        if m < 0 or n < 0:
            return -1

        if idx >= len(strs):
            return 0

        if memo[idx][m][n] != -1:
            return memo[idx][m][n]

        new_m = m - counts[idx][0]
        new_n = n - counts[idx][1]
        
        best = max(self.solve(strs, m, n, idx + 1, memo, counts), 1 + self.solve(strs, new_m, new_n, idx + 1, memo, counts))

        memo[idx][m][n] = best
        return best
