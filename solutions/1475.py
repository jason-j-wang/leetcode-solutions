#https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [-1] * len(prices)
        stack = []

        for i, p in enumerate(prices):
            while stack and p <= stack[-1][1]:
                idx, old = stack.pop()
                ans[idx] = old - p

            stack.append([i, p])

        while stack:
            idx, old = stack.pop()
            ans[idx] = old
        return ans



        