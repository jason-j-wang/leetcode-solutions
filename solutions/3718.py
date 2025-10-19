#https://leetcode.com/problems/smallest-missing-multiple-of-k/description/
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = set(nums)

        for i in range(1, 102):
            if k * i not in n:
                return k * i