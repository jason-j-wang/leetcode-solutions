#https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/?envType=daily-question&envId=2025-02-15
class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            if self.validate(i * i, i):
                ans += i * i
        return ans
        
    def validate(self, n, target, cur_sum=0):
        if target < 0 or n < target:
            return False

        if n == target:
            return True

        valid = self.validate(n // 10, target- n % 10)
        valid |= self.validate(n // 100, target- n % 100)
        valid |= self.validate(n // 1000, target- n % 1000)
        return valid