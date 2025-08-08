#https://leetcode.com/problems/soup-servings/?envType=daily-question&envId=2025-08-08
class Solution:
    def soupServings(self, n: int) -> float:
        m = (n + 24) // 25

        dp = defaultdict(dict)

        def solve(a, b):
            if a <= 0 and b <= 0:
                return 0.5

            if a <= 0:
                return 1

            if b <= 0:
                return 0

            if a in dp and b in dp[a]:
                return dp[a][b]

            prob = 0.25 * (solve(a - 4, b) + solve(a - 3, b - 1) + solve(a - 2, b - 2) + solve(a - 1, b - 3))
            dp[a][b] = prob
            return prob

        for k in range(1, m + 1):
            if solve(k, k) > 1 - 1e-5:
                return 1
        return solve(m, m)