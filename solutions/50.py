#https://leetcode.com/problems/powx-n/description/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        num = x
        neg = n < 0
        n = abs(n)

        while n != 0:
            if n % 2 == 1:
                if not neg:
                    ans *= num
                else:
                    ans /= num
            num *= num
            n //= 2
        return ans