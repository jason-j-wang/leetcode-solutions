#https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/?envType=daily-question&envId=2025-03-11
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = {}
        counts["a"] = 0
        counts["b"] = 0
        counts["c"] = 0

        left = 0
        right = 0
        ans = 0
        n = len(s)

        while right < n:
            counts[s[right]] += 1

            while counts["a"] > 0 and counts["b"] > 0 and counts["c"] > 0:
                ans += n - right
                counts[s[left]] -= 1
                left += 1
            right += 1

        return ans