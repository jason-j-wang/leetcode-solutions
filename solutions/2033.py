#https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/?envType=daily-question&envId=2025-03-26
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums.append(grid[i][j])

        nums.sort()
        n = len(nums)
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[0]) % x != 0:
                return -1

        ans = 0
        for i in range(len(nums) // 2):
            ans += (nums[n - 1 - i] - nums[i]) // x
        return ans