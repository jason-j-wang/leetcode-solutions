#https://leetcode.com/problems/minimum-time-to-make-rope-colorful/?envType=daily-question&envId=2025-11-03
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        i = 1
        ans = 0
        while i < n:
            if colors[i] == colors[i-1]:
                j = i - 1
                total = 0
                max_cost = neededTime[j]

                while j < n and colors[j] == colors[i]:
                    total += neededTime[j]
                    if neededTime[j] > max_cost:
                        max_cost = neededTime[j]
                    j += 1

                i = j
                ans += total - max_cost
            i += 1

        return ans

