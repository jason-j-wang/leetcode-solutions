#https://leetcode.com/problems/apply-operations-to-an-array/description/?envType=daily-question&envId=2025-03-01
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        idx = 0

        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i+1] and nums[i] != 0:
                nums[idx] = nums[i] * 2
                nums[i+1] = 0
                if idx != i:
                    nums[i] = 0
                idx += 1

            elif nums[i] != 0:
                nums[idx] = nums[i]
                if idx != i:
                    nums[i] = 0
                idx += 1
        return nums
            