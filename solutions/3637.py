#https://leetcode.com/problems/trionic-array-i/description/
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                valid = True
                for k in range(1, i+1):
                    if nums[k] <= nums[k-1]:
                        valid = False

                for k in range(i+1, j+1):
                    if nums[k] >= nums[k-1]:
                        valid = False

                for k in range(j+1, n):
                    if nums[k] <= nums[k-1]:
                        valid = False

                if valid:
                    return True
        return False

        