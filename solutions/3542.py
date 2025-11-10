#https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/description/?envType=daily-question&envId=2025-11-10
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ans = 0

        for n in nums:
            if n == 0:
                ans += self.empty_stack(stack)

            elif not stack or n >= stack[-1]:
                stack.append(n)

            else:
                while stack and stack[-1] > n:
                    cur_num = stack[-1]
                    while stack and stack[-1] == cur_num:
                        stack.pop()

                    ans += 1

                stack.append(n)
        ans += self.empty_stack(stack)
        return ans

    def empty_stack(self, stack):
        ans = 0
        while stack:
            cur_num = stack[-1]
            while stack and stack[-1] == cur_num:
                stack.pop()

            ans += 1
        return ans

