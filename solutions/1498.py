#https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/?envType=daily-question&envId=2025-06-29
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        mod = 10 ** 9 + 7

        right = len(nums) - 1
        for i in range(len(nums)):
            if right < i:
                return ans
            while nums[i] + nums[right] > target:
                right -= 1
                if right < i:
                    return ans     

            res = (self.pow(2, right - i)) % mod

            ans += res
            ans %= mod
        return ans

    def pow(self, n, exp):
        if exp < 0:
            return 1
        mod = 10 ** 9 + 7
        num = 1

        while exp > 0:
            if exp % 2 == 1:
                num *= n
                num %= mod
            n *= n
            n %= mod
            exp //= 2
        return num

