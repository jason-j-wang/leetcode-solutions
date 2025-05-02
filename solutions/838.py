#https://leetcode.com/problems/push-dominoes/?envType=daily-question&envId=2025-05-02
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        s = 0
        for i in range(n):
            if dominoes[i] == "R":
                s = n
            elif dominoes[i] == "L":
                s = 0

            right[i] = s

            if s > 0:
                s -= 1

        s = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == "L":
                s = n
            elif dominoes[i] == "R":
                s = 0

            left[i] = s

            if s > 0:
                s -= 1

        ans = ""
        for i in range(n):
            ans += "." if left[i] - right[i] == 0 else ("R" if left[i] - right[i] < 0 else "L")
        return ans