#https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        val = max(nums)

        left = 0
        ans = 0
        count = 0

        for i, n in enumerate(nums):
            if n == val:
                count += 1

            while count >= k:
                ans += len(nums) - i
                if nums[left] == val:
                    count -= 1
                left += 1
        return ans
        