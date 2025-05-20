#https://leetcode.com/problems/zero-array-transformation-i/description/?envType=daily-question&envId=2025-05-20
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        prefix = [0 for _ in range(n+1)]

        for l, r in queries:
            prefix[l] += 1
            prefix[r+1] -= 1
        cur = 0
        for i in range(n):
            cur += prefix[i]
            if cur < nums[i]:
                return False
        return True