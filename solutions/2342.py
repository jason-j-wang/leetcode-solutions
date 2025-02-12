#https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/?envType=daily-question&envId=2025-02-12
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1

        nums_by_digit_sum = {}

        ans = -1
        for i in range(len(nums)):
            digit_sum = self.sum_digits(nums[i])
            if digit_sum not in nums_by_digit_sum:
                nums_by_digit_sum[digit_sum] = []
            heapq.heappush(nums_by_digit_sum[digit_sum], -nums[i])

        for digit_sum in nums_by_digit_sum:
            array = nums_by_digit_sum[digit_sum]
            if len(array) > 1:
                first = -heapq.heappop(array)
                second = -heapq.heappop(array)
                ans = max(ans,first + second)
        return ans

    def sum_digits(self, num):

        ans = 0
        while num:
            ans += (num % 10)
            num //= 10

        return ans