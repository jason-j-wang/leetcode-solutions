#https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2025-03-03
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        e = []
        g = []

        for num in nums:
            if num < pivot:
                l.append(num)
            elif num == pivot:
                e.append(num)
            else:
                g.append(num)

        return l + e + g