#https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/description/?envType=daily-question&envId=2025-10-22
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        nums.sort()
        arr_max = self.sub_solve(nums, k, numOperations)

        left = 0
        ans = 0

        for right in range(n):
            while nums[right] > nums[left] + 2 * k:
                left += 1

            ans = max(ans, right - left + 1)

            if ans >= numOperations:
                ans = numOperations
                break
        
        return max(ans, arr_max)
        

    def sub_solve(self, nums, k, numOperations):
        count = Counter(nums)

        best = 0

        for val in count.keys():
            left = bisect_left(nums, val - k)
            right = bisect_right(nums, val + k) - 1
            freq = min(right - left + 1, numOperations + count[val])
            best = max(best, freq)

        return best