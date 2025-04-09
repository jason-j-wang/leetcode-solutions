#https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/?envType=daily-question&envId=2025-04-09
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()

        for n in nums:
            if n < k:
                return -1

            elif n > k:
                seen.add(n)

        return len(seen)