#https://leetcode.com/problems/longest-balanced-substring-i/description/
class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            c = defaultdict(int)
            for j in range(i, len(s)):
                c[s[j]] += 1
                num = c[s[i]]
                valid = True
                for char in c:
                    if c[char] != num:
                        valid = False
                        break

                if valid:
                    ans = max(ans, j - i + 1)
        return ans
        