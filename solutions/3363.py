#https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/description/?envType=daily-question&envId=2025-08-07
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        ans = 0
        
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        dp[n-1][n-2] = fruits[n-1][n-2]
        for j in range(n-3, -1, -1):
            for i in range(n-1, j, -1):
                
                dp[i][j] = fruits[i][j] + max(dp[i][j+1], dp[i-1][j+1], dp[i+1][j+1])
        ans += dp[n-1][0]

        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        dp[n-2][n-1] = fruits[n-2][n-1]

        for i in range(n-3, -1, -1):
            for j in range(n-1, i, -1):
                dp[i][j] = fruits[i][j] + max(dp[i+1][j], dp[i+1][j-1], dp[i+1][j+1])
        ans += dp[0][n-1]

        for i in range(n):
            ans += fruits[i][i]
        return ans