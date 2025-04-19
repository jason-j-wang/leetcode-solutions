#https://leetcode.com/problems/count-the-number-of-fair-pairs/description/?envType=daily-question&envId=2025-04-19
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.solve(nums, upper + 1) - self.solve(nums, lower)


    def solve(self, nums, threshold):
        left = 0
        right = len(nums)-1
        ans = 0

        while left < right:
            s = nums[left] + nums[right]
            if s < threshold:
                ans += right - left
                left += 1

            else:
                right -= 1
        return ans