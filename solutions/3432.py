#https://leetcode.com/problems/count-partitions-with-even-sum-difference/
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            total += n

        ans = 0
        cur =0

        for i in range(len(nums)-1):
            cur += nums[i]
            total -= nums[i]

            if abs(cur - total) % 2 == 0:
                ans += 1
        return ans