#https://leetcode.com/problems/apple-redistribution-into-boxes/description/?envType=daily-question&envId=2025-12-24
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)

        total = sum(apple)
        ans = 0
        cur = 0

        for c in capacity:
            if cur >= total:
                return ans

            ans += 1
            cur += c
        return ans
