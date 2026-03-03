#https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/?envType=daily-question&envId=2026-03-03
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        s_len = 2 ** n 

        if k < s_len // 2:
            return self.findKthBit(n - 1, k)

        if k == s_len // 2:
            return "1"

        bit = self.findKthBit(n - 1, s_len - k)
        return "1" if bit == "0" else "0"