#https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/?envType=daily-question&envId=2026-01-10
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n-1, -1, -1):
            dp[i][m] = ord(s1[i]) + dp[i+1][m]

        for i in range(m - 1, -1, -1):
            dp[n][i] = ord(s2[i]) + dp[n][i+1]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(ord(s1[i]) + dp[i+1][j], ord(s2[j]) + dp[i][j+1])

        return dp[0][0]