#https://leetcode.com/problems/number-of-zero-filled-subarrays/?envType=daily-question&envId=2025-08-19
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                ans += i - left + 1
            else:
                left = i + 1
        return ans