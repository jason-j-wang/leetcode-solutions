#https://leetcode.com/problems/find-the-maximum-sum-of-node-values/submissions/1641734361/?envType=daily-question&envId=2025-05-23
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0, 0] for i in range(n + 1)]
        dp[n][0] = -float('inf')
        dp[n][1] = 0

        for i in range(n-1, -1, -1):
            for j in range(2):
                do_xor = dp[i+1][j ^ 1] + (nums[i] ^ k)

                no_xor = dp[i+1][j] + nums[i]

                dp[i][j] = max(do_xor, no_xor)
        return dp[0][1]