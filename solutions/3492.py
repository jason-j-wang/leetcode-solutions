#https://leetcode.com/problems/maximum-containers-on-a-ship/
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        if w >  maxWeight:
            return 0

        num = maxWeight // w

        return num if num < n ** 2 else n ** 2