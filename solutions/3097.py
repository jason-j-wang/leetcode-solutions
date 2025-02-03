#https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/?envType=daily-question&envId=2025-02-03
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bit_counts = [0] * 32
        start = 0
        end = 0
        min_len = float("inf")

        while end < len(nums):
            if nums[end] >= k:
                return 1
            
            self.update_count(bit_counts, nums[end], 1)

            if self.to_int(bit_counts) >= k:
                while start < end and self.to_int(bit_counts) >= k:

                    min_len = min(min_len, end - start + 1)
                    self.update_count(bit_counts, nums[start], -1)
                    start+= 1
                    
            end += 1
        
        return -1 if min_len == float("inf") else min_len


    def update_count(self, count, num, diff):
        for i in range(32):
            if num & (1 << i):
                count[i] += diff


    def to_int(self, count):
        res = 0
        for i in range(32):
            if count[i]:
                res |= 1 << i
        return res