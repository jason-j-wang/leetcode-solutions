#https://leetcode.com/problems/count-the-hidden-sequences/description/?envType=daily-question&envId=2025-04-21
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        smallest = 0
        largest = 0
        cur = 0

        for n in differences:
            cur += n
            smallest = min(smallest, cur)
            largest = max(largest, cur)


        if largest - smallest > upper - lower:
            return 0

        return (upper - lower) - (largest - smallest) + 1