#https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/description/
class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n)]

        counts = defaultdict(int)
        counts[0] = 1

        cur = 0
        ans = 0

        for i, num in enumerate(nums):          
            cur += num
            cur %= k

            ans += counts[cur]
        
            prefix[i] = cur
            counts[cur] += 1

        left = 0

        while left < n:
            num = nums[left]
            right = bisect.bisect_right(nums, num) - 1

            dupes = 0
            for i in range(left, right + 1):
                if (num * (right - i + 1)) % k == 0:
                    ans -= dupes
                dupes += 1

            left = right + 1
        return ans