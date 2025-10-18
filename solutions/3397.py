#https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description/?envType=daily-question&envId=2025-10-18
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        if n == 0:
            return 0

        ans = 1
        nums[0] = nums[0] - k

        for i in range(1, n):
            next = nums[i - 1] + 1

            if nums[i] - k <= next and nums[i] + k >= next:
                nums[i] = next
                ans += 1
            else:
                if nums[i] - k > next:
                    nums[i] -= k
                    ans += 1
                else:
                    nums[i] += k
        return ans