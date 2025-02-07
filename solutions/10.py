#https://leetcode.com/problems/regular-expression-matching/?envType=problem-list-v2&envId=dynamic-programming
class Solution:
    # let i represent cur idx of the string
    # let j represent cur idx of regexp
    # recurrence dp[i][j] = any(dp[i+1][j+2], dp[i+1][j], dp[i][j+2])
    def isMatch(self, s: str, p: str) -> bool:
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
            if j < len(p) - 1 and p[j+1] == "*":
                return self.solve(s, p, i, j + 2, memo)

            return False
        
        if memo[i][j] != 0:
            return True if memo[i][j] == 1 else False

        # check if there is a *
        if j < len(p) - 1 and p[j+1] == "*":
            # 0 instance case
            valid = self.solve(s, p, i, j + 2, memo)
            char = p[j]
            
            if p[j] == "." or s[i] == p[j]:
                valid = valid or self.solve(s, p, i + 1, j + 2, memo) or self.solve(s, p, i + 1, j, memo)

            memo[i][j] = 1 if valid else -1
            memo[i][j+1] = memo[i][j]
            return valid
        else:
            if p[j] == "." or s[i] == p[j]:
                memo[i][j] = 1 if self.solve(s, p, i + 1, j + 1, memo) else -1
                return memo[i][j] == 1
            else:
                memo[i][j] = -1
                return False