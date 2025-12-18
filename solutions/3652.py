#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/description/?envType=daily-question&envId=2025-12-18
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        strat_sum = [0] * n
        price_sum = [0] * n

        strat_sum[0] = strategy[0] * prices[0]
        price_sum[0] = prices[0]

        for i in range(1, n):
            strat_sum[i] = strat_sum[i-1] + strategy[i] * prices[i]
            price_sum[i] = price_sum[i-1] + prices[i]

        ans = strat_sum[-1]

        for i in range(n - k + 1):
            left = strat_sum[i-1] if i > 0 else 0
            right = strat_sum[n-1] - strat_sum[i + k - 1]
            mid = price_sum[i + k - 1] - price_sum[i + k // 2 - 1]
            ans = max(ans, left + mid + right)
        return ans
