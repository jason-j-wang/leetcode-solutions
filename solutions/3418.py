#https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/?envType=daily-question&envId=2026-04-02
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])

        dp = [[[-inf for _ in range(3)] for _ in range(m)] for _ in range(n)]

        dp[0][0][0] = coins[0][0]
        for i in range(1, 3):
            dp[0][0][i] = max(coins[0][0], 0)

        for i in range(1, n):
            for k in range(3):
                dp[i][0][k] = dp[i - 1][0][k] + coins[i][0]
                if k > 0:
                    dp[i][0][k] = max(dp[i][0][k], dp[i - 1][0][k - 1] + max(coins[i][0], 0))

        for j in range(1, m):
            for k in range(3):
                dp[0][j][k] = dp[0][j - 1][k] + coins[0][j]
                if k > 0:
                    dp[0][j][k] = max(dp[0][j][k], dp[0][j - 1][k - 1] + max(coins[0][j], 0))


        for i in range(1, n):
            for j in range(1, m):
                for k in range(3):
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k])
                    dp[i][j][k] += coins[i][j]

                    if k > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1], dp[i][j - 1][k - 1])

        return dp[n-1][m-1][2]


        
