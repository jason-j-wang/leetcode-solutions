#https://leetcode.com/problems/wildcard-matching/?envType=problem-list-v2&envId=dynamic-programming
class Solution:
    # let i be the cur idx of string
    # let j be cur idx of pattern
    # dp[i][j] = any(dp[i, j + 1], dp[i + 1, j], dp[i + 1, j + 1])
    def isMatch(self, s: str, p: str) -> bool:
        if p == "":
            return s == ""

        n = len(s)
        m = len(p)
        memo = [[0 for _ in range(m)] for _ in range(n)]
        print(memo)

        return self.solve(s, p, 0, 0, memo)


    def solve(self, s, p, i, j, memo):
        #base cases
        if j == len(p):
            return i == len(s) and j == len(p)

        if i == len(s):
            if i == len(s) and j == len(p):
                return True
            # case where last char in regexp is a *
            if j < len(p) and p[j] == "*":
                return self.solve(s, p, i, j + 1, memo)

            return False
        
        if memo[i][j] != 0:
            return True if memo[i][j] == 1 else False

        # check if there is a *
        if p[j] == "*":
            # 0 instance case
            valid = self.solve(s, p, i, j + 1, memo) or self.solve(s, p, i + 1, j + 1, memo) or self.solve(s, p, i + 1, j, memo)
           
            memo[i][j] = 1 if valid else -1
            return valid
        else:
            if p[j] == "?" or s[i] == p[j]:
                memo[i][j] = 1 if self.solve(s, p, i + 1, j + 1, memo) else -1
                return memo[i][j] == 1
            else:
                memo[i][j] = -1
                return False