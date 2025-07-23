#https://leetcode.com/problems/maximum-score-from-removing-substrings/description/?envType=daily-question&envId=2025-07-23
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        ans = 0

        for c in s:
            if stack:
                if x > y:
                    if stack[-1] == "a" and c == "b":
                        ans += x
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    if stack[-1] == "b" and c == "a":
                        ans += y
                        stack.pop()
                    else:
                        stack.append(c)

            else:
                stack.append(c)
       

        second = stack
        stack = []
        for c in second:
            if stack:
                if x <= y:
                    if stack[-1] == "a" and c == "b":
                        ans += x
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    if stack[-1] == "b" and c == "a":
                        ans += y
                        stack.pop()
                    else:
                        stack.append(c)

            else:
                stack.append(c)
        return ans