#https://leetcode.com/problems/maximum-balanced-shipments/
class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        ans = 0
        cur_max = 0

        for i in range(len(weight)):
            if weight[i] >= cur_max:
                cur_max = weight[i]
            else:
                ans += 1
                cur_max = 0
        return ans