#https://leetcode.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] -1] != nums[i]:
                temp = nums[nums[i] -1]
                nums[nums[i] -1] = nums[i]
                nums[i] = temp
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
        