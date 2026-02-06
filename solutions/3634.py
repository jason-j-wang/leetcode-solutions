#https://leetcode.com/problems/minimum-removals-to-balance-array/description/?envType=daily-question&envId=2026-02-06
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        right = 0
        ans = 0
        for i in range(n):
            while right < n and nums[i] * k >= nums[right]:
                right += 1
            ans = max(ans, right- i)
        return n - ans
