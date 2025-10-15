#https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description/?envType=daily-question&envId=2025-10-15
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 0
        ans = 0
        cur = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                ans = max(ans, cur // 2, min(prev, cur))
                prev = cur
                cur = 1
        return max(ans, cur // 2, min(prev, cur))