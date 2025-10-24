#https://leetcode.com/problems/next-greater-numerically-balanced-number/description/?envType=daily-question&envId=2025-10-24
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if n == 0:
            return 1
        for i in range(n + 1, n * 100):
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i