#https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/?envType=daily-question&envId=2025-07-30
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = max(nums)
        ans = 0
        cur = 0

        for num in nums:
            if num == n:
                cur += 1

            else:
                ans = max(ans, cur)
                cur = 0
        return max(ans, cur)