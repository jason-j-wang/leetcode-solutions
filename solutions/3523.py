#https://leetcode.com/problems/make-array-non-decreasing/description/
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans = 0
        cur = nums[0]
        i = 0
        while i < len(nums):
            if nums[i] < cur:
                while nums[i] < cur:
                    i += 1
                    if i >= len(nums):
                        return ans
                cur = nums[i]
                ans += 1
                i += 1
            else:
                ans += 1
                
                cur = nums[i]
                i += 1
        return ans
            