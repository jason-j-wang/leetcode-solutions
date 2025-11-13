#https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/?envType=daily-question&envId=2025-11-13
class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        counter = 0
        n = len(s)

        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                continue

            if s[i+1] == "0":
                counter += 1
            ans += counter

        return ans