#https://leetcode.com/problems/divide-array-into-equal-pairs/description/?envType=daily-question&envId=2025-03-17
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        for n in counts:
            if counts[n] % 2 != 0:
                return False
        return True