#https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/description/?envType=daily-question&envId=2025-07-18
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        for i in range(n):
            nums[i] = -nums[i]

        first = nums[:n]
        second = nums[2*n:]
        heapq.heapify(first)
        heapq.heapify(second)

        first_sums = [0 for _ in range(n+1)]
        second_sums = [0 for _ in range(n+1)]
        
        first_sums[0] = -sum(first)
        second_sums[0] = sum(second)

        for i in range(n, 2 * n):
            heapq.heappush(first, -nums[i])
            heapq.heappush(second, nums[3 * n - 1 - i])

            largest_first = heapq.heappop(first)
            smallest_second = heapq.heappop(second)

            base_idx = i - n + 1

            first_sums[base_idx] = first_sums[base_idx - 1] + largest_first + nums[i]
            second_sums[base_idx] = second_sums[base_idx - 1] - smallest_second + nums[3 * n - 1 - i]

        ans = float('inf')

        for i in range(n+1):
            diff = first_sums[i] - second_sums[n - i]
            if diff < ans:
                ans = diff
        return ans