#https://leetcode.com/problems/construct-smallest-number-from-di-string/description/?envType=daily-question&envId=2025-02-18
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        cur_num = 1
        ans = ""
        stack = []

        for p in pattern:
            stack.append(cur_num)
            cur_num += 1

            if p == "I":
                while stack:
                    ans += str(stack.pop())
        stack.append(cur_num)
        while stack:
            ans += str(stack.pop())

        return ans
