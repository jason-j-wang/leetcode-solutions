#https://leetcode.com/problems/remove-zeros-in-decimal-representation/description/
class Solution:
    def removeZeros(self, n: int) -> int:
        c = []
        for s in str(n):
            if s != "0":
                c.append(s)
        return int("".join(c))