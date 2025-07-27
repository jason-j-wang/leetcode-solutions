#https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/?envType=daily-question&envId=2025-07-27
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        left = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                left = nums[i-1]

            if i < n - 1:
                if left > nums[i] and nums[i+1] > nums[i]:
                    ans += 1

                elif left < nums[i] and nums[i+1] < nums[i]:
                    ans += 1
        return ans
            