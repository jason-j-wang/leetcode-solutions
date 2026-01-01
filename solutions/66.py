#https://leetcode.com/problems/plus-one/description/?envType=daily-question&envId=2026-01-01
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        if digits[0] == 0:
            return [1] + digits