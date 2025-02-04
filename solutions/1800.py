#https://leetcode.com/problems/maximum-ascending-subarray-sum/description/?envType=daily-question&envId=2025-02-04
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = ans
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += nums[i]
            else:
                ans = max(ans, cur)
                cur = nums[i]
        ans = max(ans, cur)
        return ans