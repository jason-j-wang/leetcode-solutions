#https://leetcode.com/problems/complement-of-base-10-integer/description/?envType=daily-question&envId=2026-03-11
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return ~n & ((1 << n.bit_length()) - 1) if n != 0 else 1