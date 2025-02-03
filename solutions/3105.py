#https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc = 0
        max_dec = 0
        inc_ans = 1
        dec_ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_ans += 1
                max_dec = max(dec_ans, max_dec)
                dec_ans = 1
            elif nums[i] < nums[i-1]:
                dec_ans += 1
                max_inc = max(max_inc, inc_ans)
                inc_ans = 1
            else:
                max_dec = max(dec_ans, max_dec)
                max_inc = max(max_inc, inc_ans)
                dec_ans = 1
                inc_ans = 1
        max_dec = max(dec_ans, max_dec)
        max_inc = max(max_inc, inc_ans)

        return max(max_dec, max_inc)
        