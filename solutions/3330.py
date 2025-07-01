#https://leetcode.com/problems/find-the-original-typed-string-i/description/?envType=daily-question&envId=2025-07-01
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                ans += 1
        return ans