#https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/?envType=daily-question&envId=2025-07-28
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0

        dp = [0 for _ in range(2 ** 17)]

        dp[0] = 1

        for n in nums:
            for i in range(max_or, -1, -1):
                dp[n | i] += dp[i]

            max_or |= n

        return dp[max_or]