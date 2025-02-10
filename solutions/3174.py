#https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10
class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []
        string_digits = [str(i) for i in range(10)]

        for char in s:
            if char in string_digits:
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "".join(stack) if stack else ""