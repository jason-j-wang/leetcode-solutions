#https://leetcode.com/problems/power-of-four/description/?envType=daily-question&envId=2025-08-15
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        if n.bit_count() != 1:
            return False

        return (n.bit_length() - 1) % 2 == 0