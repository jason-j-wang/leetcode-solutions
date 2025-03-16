#https://leetcode.com/problems/minimum-time-to-repair-cars/?envType=daily-question&envId=2025-03-16
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = (cars ** 2) * max(ranks)
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            if self.valid(ranks, cars, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
        
    def valid(self, ranks, cars, time):
        fixed = 0

        for r in ranks:
            fixed += int(sqrt(time / r))

            if fixed >= cars:
                return True
        return False