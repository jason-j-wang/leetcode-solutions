#https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/?envType=daily-question&envId=2026-02-23
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k == 19 or k == 20 or k > len(s):
            return False

        seen = set()
        num = 0
        mask = 2 ** k - 1

        for i in range(k):
            num <<= 1
            if s[i] == "1":
                num |= 1

        seen.add(num)

        for i in range(k, len(s)):
            num = ((num << 1) & mask)
            if s[i] == "1":
                num |= 1

            seen.add(num)
        return len(seen) == 2 ** k