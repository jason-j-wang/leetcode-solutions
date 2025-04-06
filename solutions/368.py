#https://leetcode.com/problems/largest-divisible-subset/description/?envType=daily-question&envId=2025-04-06
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        dp = [1 for i in range(len(nums))]
        prev = [-1 for i in range(len(nums))]

        best = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > dp[best]:
                best = i

        ans = []
        while best >= 0:
            ans.append(nums[best])
            best = prev[best]

        return ans