#https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/?envType=daily-question&envId=2026-01-25
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = inf
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans