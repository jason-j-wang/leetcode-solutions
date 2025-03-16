#https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n > 0:
                s.add(n)
        if not s:
            return max(nums)
        else:
            return sum(s)