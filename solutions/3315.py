#https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/description/?envType=daily-question&envId=2026-01-21
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            x = -1
            d = 1

            while (nums[i] & d) != 0:
                x = nums[i] - d
                d <<= 1
            nums[i] = x
        return nums