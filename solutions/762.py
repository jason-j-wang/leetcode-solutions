#https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/?envType=daily-question&envId=2026-02-20
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        count = 0
        for i in range(left, right + 1):
            if i.bit_count() in primes:
                count += 1
        return count