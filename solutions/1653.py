#https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2026-02-07
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        right_a = [0 for _ in range(n)]
        left_b = [0 for _ in range(n)]
        a, b = 0, 0
        for i in range(n - 1, -1, -1):
            right_a[i] = a
            if s[i] == 'a':
                a += 1
            
        for i in range(n):
            left_b[i] = b
            if s[i] == 'b':
                b += 1
            
        ans = inf

        for i in range(n):
            ans = min(ans, right_a[i] + left_b[i])
        return ans