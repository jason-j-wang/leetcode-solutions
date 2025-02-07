#https://leetcode.com/problems/jump-game/description/?envType=problem-list-v2&envId=greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_true = n - 1

        for i in range(n-2, -1, -1):
            if i + nums[i] >= last_true:
                last_true = i

        return last_true == 0
