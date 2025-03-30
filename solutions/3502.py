#https://leetcode.com/problems/minimum-cost-to-reach-every-position/description/
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []
        m = cost[0]
        for i in range(len(cost)):
            m = min(cost[i], m)
            ans.append(m)
        return ans