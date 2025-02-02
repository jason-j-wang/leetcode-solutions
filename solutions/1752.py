#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2025-02-02
class Solution:
    def check(self, nums: List[int]) -> bool:
        rotated = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if rotated:
                    return False
                rotated = True
            if rotated:
                if nums[i] > nums[0]:
                    return False
        return True