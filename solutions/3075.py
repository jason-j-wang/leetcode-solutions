#https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2025-12-25
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        ans = 0
        sub = 0
        for i in range(k):
            if happiness[i] - sub > 0:
                ans += happiness[i] - sub
                sub += 1
        return ans