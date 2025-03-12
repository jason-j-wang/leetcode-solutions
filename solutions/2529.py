#https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/?envType=daily-question&envId=2025-03-12
class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        left = 0
        idx = len(nums)
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= 0:
                right = mid - 1
                idx = mid
            else:
                left = mid + 1
        negs = idx


        left = 0
        idx = len(nums)
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1
                idx = mid

        pos = len(nums) - idx

        return max(pos, negs)