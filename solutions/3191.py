#https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/?envType=daily-question&envId=2025-03-19
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        swaps = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                swaps += 1
                nums[i] = (nums[i] + 1) % 2
                nums[i+1] = (nums[i+1] + 1) % 2
                nums[i+2] = (nums[i+2] + 1) % 2
        
        if nums[-1] == 0 or nums[-2] == 0 or nums[-3] == 0:
            return -1
        return swaps