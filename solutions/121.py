#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = float('inf')
        cur_max = 0

        for i in range(len(prices)):
            cur_min = min(cur_min, prices[i])
            cur_max = max(cur_max, prices[i] - cur_min)
        return cur_max