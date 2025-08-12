#https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/?envType=daily-question&envId=2025-08-12
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        for i in range(1, n + 1):
            num = i ** x
            if num > n:
                break
            for j in range(n, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % mod
        return dp[n]
