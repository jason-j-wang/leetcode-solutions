#https://leetcode.com/problems/power-of-three/description/?envType=daily-question&envId=2025-08-13
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        exp = (log(1 << 31) / log(3)) // 1
        max_num = pow(3, exp)
        return max_num % n == 0