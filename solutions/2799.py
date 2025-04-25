#https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=daily-question&envId=2025-04-24
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            seen.add(n)
        distinct = len(seen)

        left = 0
        right = 0
        cur = defaultdict(int)
        seen = set()
        ans = 0

        while right < len(nums):
            num = nums[right]
            cur[num] += 1
            seen.add(num)

            while len(seen) == distinct:
                ans += len(nums) - right
                l = nums[left]
                cur[l] -= 1
                if cur[l] == 0:
                    seen.remove(l)
                left += 1
            right += 1
        return ans