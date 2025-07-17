#https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/?envType=daily-question&envId=2025-07-17
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 2

        for i in range(k):
            dp = [0 for _ in range(k)]

            for j in range(n):
                num = nums[j] % k
                other_num = (i - num + k) % k
                dp[num] = dp[other_num] + 1

                if dp[num] > ans:
                    ans = dp[num]
        return ans