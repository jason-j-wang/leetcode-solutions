#https://leetcode.com/problems/longest-balanced-substring-ii/description/
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        #single letter
        cur = ''
        cur_len = 0
        for c in s:
            if c == cur:
                cur_len += 1
            else:
                ans = max(ans, cur_len)
                cur_len = 1
                cur = c
        ans = max(ans, cur_len)

        #two letters
        letters = ['a', 'b', 'c']
        
        for i in range(3):
            for j in range(i+1, 3):
                l1 = letters[i]
                l2 = letters[j]
                prefix = {0: -1}
                l1count = 0
                l2count = 0

                for k in range(n):
                    ch = s[k]
                    if ch != l1 and ch != l2:
                        prefix = {0: k}
                        l1count = 0
                        l2count = 0
                    else:
                        if ch == l1:
                            l1count += 1
                        else:
                            l2count += 1
                        
                        diff = l1count - l2count
                        if diff in prefix:
                            ans = max(ans, k - prefix[diff])
                        else:
                            prefix[diff] = k             
 
        #all letters
        prefix = {}
        prefix[(0, 0)] = -1
        counts = [0, 0, 0]
        for i in range(n):
            ch = s[i]
            counts[ord(ch)- ord('a')] += 1

            c = counts[0] - counts[2]
            b = counts[0] - counts[1]
            t = (b, c)
            if t in prefix:
                ans= max(ans, i - prefix[t])
            else:
                prefix[t] = i
        return ans


                