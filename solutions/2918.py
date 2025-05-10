#https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/?envType=daily-question&envId=2025-05-10
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = False
        z2 = False

        sum1 = 0
        sum2 = 0

        for n in nums1:
            if n == 0:
                z1 = True
                sum1 += 1
            else:
                sum1 += n

        for n in nums2:
            if n == 0:
                z2 = True
                sum2 += 1
            else:
                sum2 += n

        if sum1 == sum2:
            return sum1

        elif sum1 > sum2:
            return sum1 if z2 else -1

        else:
            return sum2 if z1 else -1