#https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        ans = 0
        for n in c:
            if c[n] % k == 0:
                ans += n * c[n]
        return ans