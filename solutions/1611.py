#https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=daily-question&envId=2025-11-08
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        
        ans = 0
        k = 0
        mask = 1
        
        while mask <= n:
            if n & mask:
                ans = 2 ** (k + 1) - 1 - ans
                
            mask <<= 1
            k += 1
        
        return ans
