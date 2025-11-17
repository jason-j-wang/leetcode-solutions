#https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/?envType=daily-question&envId=2025-11-17
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -k - 1
        for i, n in enumerate(nums):
            if n == 1:
                if i - last <= k:
                    return False
                last = i
        return True