#https://leetcode.com/problems/minimum-penalty-for-a-shop/description/?envType=daily-question&envId=2025-12-26
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pen = 0

        for c in customers:
            if c == "N":
                pen += 1
        best = pen
        n = len(customers)
        ans = n

        for i in range(n - 1, -1, -1):
            c = customers[i]
            if c == "N":
                pen -= 1
            else:
                pen += 1
           
            if pen <= best:
                best = pen
                ans = i
        return ans