#https://leetcode.com/problems/maximum-alternating-sum-of-squares/description/
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = abs(nums[i])

        nums.sort()

        ans = 0

        for i in range(n):
            if i < n // 2:
                ans -= nums[i] ** 2
            else:
                ans += nums[i] ** 2
        return ans