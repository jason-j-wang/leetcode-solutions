#https://leetcode.com/problems/build-array-from-permutation/?envType=daily-question&envId=2025-05-06
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]