#https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/?envType=daily-question&envId=2025-04-05
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.solve(nums, 0, 0)

    def solve(self, nums, idx, xor):
        if idx == len(nums):
            return xor

        return self.solve(nums, idx + 1, xor ^ nums[idx]) + self.solve(nums, idx + 1, xor)