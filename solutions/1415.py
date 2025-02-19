#https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2025-02-19\
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ["a", "b", "c"]

        ans = []
        self.build(letters, n, "", ans)

        if len(ans) >= k:
            return ans[k -1]
        return ""


    def build(self, letters, n, s, ans):
        if len(s) == n:
            ans.append(s)
            return

        for c in letters:
            if len(s) == 0 or s[-1] != c:
                self.build(letters, n, s + c, ans)