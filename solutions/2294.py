#https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/?envType=daily-question&envId=2025-06-19
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur_min = nums[0]
        ans = 1

        for n in nums:
            if n - cur_min > k:
                cur_min = n
                ans += 1
        return ans