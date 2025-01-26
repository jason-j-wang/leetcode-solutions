#https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/?envType=daily-question&envId=2025-01-26
class Solution:
    def maximumLength(self, s: str) -> int:
        left = 1
        right = 50
        best = -1
        while left <= right:
            mid = left + ((right - left) // 2)

            if (self.validate(s, mid)):
                left = mid + 1
                best = mid
            else:
                right = mid - 1
        return best

    def validate(self, s, num):
        char = s[0]
        counts = defaultdict(int)

        for i in range(1, len(s)):
            if len(char) == num:
                counts[char] += 1
                char = char[1:]

            if len(char) > 0 and s[i] == char[0]:
                char += s[i]
            else:
                char = s[i]
        if len(char) == num:
            counts[char] += 1
            char = char[1:]

        for k in counts.keys():
            if counts[k] >= 3:
                return True
        return False