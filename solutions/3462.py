#https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        all_nums = []
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                all_nums.append((grid[i][j], i))

        all_nums.sort()
        counts = defaultdict(int)
        used = 0
        max_sum = 0
        idx = len(all_nums) - 1

        while True:
            if used == k:
                return max_sum

            if idx == -1:
                return max_sum

            num, row = all_nums[idx]
            if counts[row] < limits[row]:
                max_sum += num
                counts[row] += 1
                used += 1
            idx -= 1
        return max_sum
                