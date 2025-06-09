#https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/?envType=daily-question&envId=2025-06-09
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        num = 1
        k -= 1

        while k > 0:
            steps = self.count(n, num, num + 1)
            if steps <= k:
                num += 1
                k -= steps
            else:
                num *= 10
                k -= 1
        return num
        

    def count(self, n, p1, p2):
        steps = 0

        while p1 <= n:
            steps += min(n + 1, p2) - p1
            p1 *= 10
            p2 *= 10
        return steps
        
