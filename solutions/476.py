#https://leetcode.com/problems/number-complement/description/
class Solution:
    def findComplement(self, num: int) -> int:
        return ~num & ((1 << num.bit_length()) - 1) if num != 0 else 1