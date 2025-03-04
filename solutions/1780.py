#https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/?envType=daily-question&envId=2025-03-04
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        p = 15
        while n > 0 and p >= 0:
            if n >= 3 ** p:
                n -= 3 ** p
            p -= 1

        return n == 0