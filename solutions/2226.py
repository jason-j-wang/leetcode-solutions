#https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/?envType=daily-question&envId=2025-03-14
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = sum(candies) // k
        best = 0

        while left <= right:
            mid = left + (right - left) // 2
            if self.validate(candies, k, mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best


    def validate(self, candies, k, num):
        children = 0
        for c in candies:
            children += c // num
            if children >= k:
                return True
        return False
        