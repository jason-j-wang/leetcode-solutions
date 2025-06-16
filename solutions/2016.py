#https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/?envType=daily-question&envId=2025-06-16
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = float('inf')
        ans = -1

        for n in nums:
            if n - min_num > ans and n - min_num != 0:
                ans = n - min_num

            if n < min_num:
                min_num = n

        return ans