#https://leetcode.com/problems/maximum-erasure-value/description/?envType=daily-question&envId=2025-07-22
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cur_sum = 0
        left = 0
        counts = defaultdict(int)
        ans = 0

        for right in range(len(nums)):
            num = nums[right]
            cur_sum += num
            counts[num] += 1

            while left < right and counts[num] > 1:
                l = nums[left]
                cur_sum -= l
                counts[l] -= 1
                left += 1
            
            if cur_sum > ans:
                ans = cur_sum
        return ans