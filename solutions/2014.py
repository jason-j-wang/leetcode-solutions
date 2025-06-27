#https://leetcode.com/problems/longest-subsequence-repeated-k-times/description/?envType=daily-question&envId=2025-06-27
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""
        letters = []
        counts = Counter(s)

        for key in counts:
            if counts[key] >= k:
                letters.append(key)

        letters.sort(reverse=True)

        q = deque(letters)

        while q:
            pattern = q.popleft()
            if len(pattern) > len(ans):
                ans = pattern

            for char in letters:
                candidate = pattern + char
                if self.find(s, candidate) >= k:
                    q.append(candidate)
        return ans

    
    def find(self, s, pattern):
        total = 0
        i = 0

        for char in s:
            if char == pattern[i]:
                i += 1
                if (i == len(pattern)):
                    i = 0
                    total += 1
        return total
