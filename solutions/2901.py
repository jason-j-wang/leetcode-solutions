#https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/description/?envType=daily-question&envId=2025-05-16
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        next_left = [-1 for _ in range(n)]
        dp = [1 for _ in range(n)]
        best = 0

        for i in range(1, n):
            for j in range(i):
                if groups[i] != groups[j] and self.hamming(words[i], words[j]) and dp[j] + 1 > dp[i]:
                    next_left[i] = j
                    dp[i] = dp[j] + 1
            if dp[i] > dp[best]:
                best = i
        
        ans = []
        i = best
        while i >= 0:
            ans.append(words[i])
            i = next_left[i]
        return ans[::-1]



    def hamming(self, a, b):
        if len(a) != len(b):
            return False

        diff = 0

        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1

            if diff > 1:
                return False
        return diff == 1