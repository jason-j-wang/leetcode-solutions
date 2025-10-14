#https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/?envType=daily-question&envId=2025-10-14
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        cur = 1
        prev = 0
        ans = 0

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                prev = cur
                cur = 1
            ans = max(ans, cur // 2, min(prev, cur))
        return ans >= k