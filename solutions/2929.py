#https://leetcode.com/problems/distribute-candies-among-children-ii/description/?envType=daily-question&envId=2025-06-01
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return self.calc(n + 2) - 3 * self.calc(n - limit + 1) + 3 * self.calc(n - (limit + 1) * 2 + 2) - self.calc(n - 3 * (limit + 1) + 2)
        
    def calc(self, x):
        if x < 0:
            return 0
        return x * (x - 1) // 2