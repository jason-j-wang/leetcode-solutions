#https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/?envType=daily-question&envId=2025-02-26
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        best = 0
        pos_cur = 0
        neg_cur = 0
        for n in nums:
            pos_cur += n
            neg_cur += n
            if pos_cur < 0:
                pos_cur = 0

            if neg_cur > 0:
                neg_cur = 0
            best = max(best, pos_cur, -neg_cur)
        return best

