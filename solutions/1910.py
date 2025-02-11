#https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/?envType=daily-question&envId=2025-02-11
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for c in s:
            stack.append(c)

            if len(stack) >= len(part) and "".join(stack[-len(part):]) == part:
                for i in range(len(part)):
                    stack.pop()

        return "".join(stack)