#https://leetcode.com/problems/rotate-string/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            if s[i] == goal[0]:
                new_str = s[i:] + s[0:i]
                if new_str == goal:
                    return True
        return False
        