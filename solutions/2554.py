#https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = set(banned)

        count = 0
        total = 0
        for i in range(1, n + 1):
            if i in s:
                continue
            
            total += i
            
            if total > maxSum:
                break
            count += 1
        return count