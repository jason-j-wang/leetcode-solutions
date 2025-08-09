#https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2025-08-09
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))