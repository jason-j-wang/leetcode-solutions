#https://leetcode.com/problems/longest-nice-subarray/description/?envType=daily-question&envId=2025-03-18
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        used = 0
        best = 1
        while right < len(nums):

            while used & nums[right] != 0:
                used ^= nums[left]
                left += 1

            used |= nums[right]
            best = max(best, right - left + 1)
            right += 1
        return best
