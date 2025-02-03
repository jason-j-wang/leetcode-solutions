#https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        new_str = s[0:2]

        for i in range(2, len(s)):
            if s[i] == new_str[-1] and s[i] == new_str[-2]:
                continue
            else:
                new_str += s[i]
        return new_str
        