#https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/description/
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        best = 0
        for a in range(len(s)):
            for b in range(a-1, len(s)+1):
                for c in range(len(t)):
                    for d in range(c-1, len(t)+1):
                        string = s[a:b] + t[c:d]
                        if self.valid(string):
                            best = max(len(string), best)
        return best


    def valid(self, s):
        return s == s[::-1]
        