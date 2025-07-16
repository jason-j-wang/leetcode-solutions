#https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/?envType=daily-question&envId=2025-07-16
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evens = 0
        odds = 0
        odd_start = 0
        even_start = 0
        base = min(2, len(nums))

        for n in nums:
            if n % 2 == 0:
                evens += 1

                if odd_start % 2 == 1:
                    odd_start += 1
                
                if even_start % 2 == 0:
                    even_start += 1
            else:
                odds += 1
                if odd_start % 2 == 0:
                    odd_start += 1
                
                if even_start % 2 == 1:
                    even_start += 1
        return max(evens, odd_start, even_start, odds, base)