#https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/?envType=daily-question&envId=2026-02-01
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n1, n2 = inf, inf
        for i in range(len(nums) - 1, 0, -1):
            n = nums[i]
            if n < n1:
                n2 = n1
                n1 = n
            elif n < n2:
                n2 = n

        return nums[0] + n1 + n2