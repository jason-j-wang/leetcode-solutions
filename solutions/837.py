#https://leetcode.com/problems/new-21-game/description/?envType=daily-question&envId=2025-08-17
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        cur_sum = 1 if k > 0 else 0
        for i in range(1, n + 1):
            dp[i] = cur_sum / maxPts
            if i < k:
                cur_sum += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                cur_sum -= dp[i - maxPts]
        return sum(dp[k:])