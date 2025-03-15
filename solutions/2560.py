#https://leetcode.com/problems/house-robber-iv/?envType=daily-question&envId=2025-03-15
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left = min(nums)
        right = max(nums)
        ans = right

        while left <= right:
            mid = left + (right - left) // 2

            if self.valid(nums, k, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def valid(self, nums, k, limit):
        i = 0
        total = 0
        while i < len(nums):
            if nums[i] <= limit:
                total += 1
                i += 2
            else:
                i += 1

            if total == k:
                return True

        return False