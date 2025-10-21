#https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/description/?envType=daily-question&envId=2025-10-21
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        max_num = max(nums)

        interval_counts = [0 for _ in range(max_num + 2)]
        num_counts = [0 for _ in range(max_num + 1)]

        for num in nums:
            interval_counts[max(0, num - k)] += 1
            interval_counts[min(max_num + 1, num + k + 1)] -= 1

            num_counts[num] += 1

        ans = 0
        cur = 0

        for i in range(max_num + 1):
            num_count = num_counts[i]

            cur += interval_counts[i]
            ans = max(ans, min(num_count + numOperations, cur))

        return ans
        