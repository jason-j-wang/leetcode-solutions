#https://leetcode.com/problems/count-good-numbers/description/?envType=daily-question&envId=2025-04-13
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return self.quick(5, (n+1)//2) * self.quick(4, n // 2) % mod
        

    def quick(self, n, e):
        mod = 10 ** 9 + 7
        ans = 1
        num = n

        while e > 0:
            if e % 2 == 1:
                ans = ans * num % mod
            num = num * num % mod
            e //= 2

        return ans
    
                