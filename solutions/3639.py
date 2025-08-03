#https://leetcode.com/problems/minimum-time-to-activate-string/description/
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        orders = []
        cur = 0
        n = len(s)

        for i in range(len(order)):
            
            o = order[i]
            bisect.insort(orders, o)

            idx = self.search(orders, o)
            if idx == len(orders) - 1:
                after = n - o
            else:
                after = orders[idx+1] - o
            
            if idx == 0:
                before = o + 1
            else:
                before = o - orders[idx-1]

            cur += before * after

            if cur >= k:
                return i
        return -1
            



    def search(self, orders, num):
        left = 0
        right = len(orders) - 1

        while left <= right:
            mid = (left + right) // 2
            if orders[mid] == num:
                return mid
            elif orders[mid] > num:
                right = mid - 1
            else:
                left = mid + 1
        return -1