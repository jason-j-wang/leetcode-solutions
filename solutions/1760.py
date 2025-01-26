#https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        left = 1
        right = 10 ** 9

        mid = 0
        ans = 0

        while (left <= right):
            mid = (left + right) // 2
            if self.validate(nums, maxOperations, mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans



    def validate(self, nums, maxOperations, penalty):
        ops = 0

        for n in nums:
            if n > penalty:
                ops += ((n + penalty -1) // penalty) - 1
            if ops > maxOperations:
                return False
        return True