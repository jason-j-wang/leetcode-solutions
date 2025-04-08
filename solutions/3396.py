#https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/?envType=daily-question&envId=2025-04-08
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in seen:
                return (i+3) // 3
            seen.add(nums[i])
        return 0