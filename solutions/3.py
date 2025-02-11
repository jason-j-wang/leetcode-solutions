#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        best = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count[s[right]] > 1 and left < right:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)

        return best
