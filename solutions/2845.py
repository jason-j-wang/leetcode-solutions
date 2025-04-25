#https://leetcode.com/problems/count-of-interesting-subarrays/description/?envType=daily-question&envId=2025-04-25
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        prefix = 0
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                prefix += 1
            ans += d[(prefix - k + modulo) % modulo]
            d[prefix % modulo] += 1
        return ans

            
