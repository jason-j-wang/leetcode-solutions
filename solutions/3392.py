#https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/?envType=daily-question&envId=2025-04-27
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        left, right = 0, 2
        while right < len(nums):
            if (nums[left] + nums[right]) * 2 == nums[left + 1]:
                ans += 1
            left += 1
            right += 1
        return ans