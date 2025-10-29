#https://leetcode.com/problems/smallest-number-with-all-set-bits/description/?envType=daily-question&envId=2025-10-29
class Solution:
    def smallestNumber(self, n: int) -> int:
        exp = log(n) / log(2)
        if exp % 1 == 0:
            exp += 1
        return 2 ** int(ceil(exp)) - 1