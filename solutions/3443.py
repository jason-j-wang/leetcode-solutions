#https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0, 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "N":
                y += 1
            elif s[i] == "S":
                y -= 1
            elif s[i] == "E":
                x += 1
            elif s[i] == "W":
                x -= 1
            ans = max(ans, min(abs(y) + abs(x) + k * 2, i + 1))
        return ans