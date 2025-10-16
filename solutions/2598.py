#https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/editorial/?envType=daily-question&envId=2025-10-16
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counts = [0 for _ in range(value)]

        for num in nums:
            counts[num % value] += 1

        m = min(counts)

        for i in range(value):
            if counts[i] == m:
                return i + value * counts[i]
        