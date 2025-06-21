#https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/submissions/1671150407/?envType=daily-question&envId=2025-06-21
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = Counter(word)
        ans = len(word)
        for thresh in counts.values():
            deleted = 0

            for num in counts.values():
                if thresh > num:
                    deleted += num
                elif num > thresh + k:
                    deleted += num - (thresh + k)
            ans = min(ans, deleted)
        return ans