#https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/?envType=daily-question&envId=2025-02-25
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        total = 0
        prefix = 0
        odd = 0
        even = 1

        for n in arr:
            prefix += n
            if prefix % 2 == 0:
                total += odd
                even += 1
            else:
                total += even
                odd += 1
            total %= (10 ** 9 + 7)
        return total