#https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/?envType=daily-question&envId=2025-02-03
class Solution:
    def minChanges(self, s: str) -> int:
        cur_bit = s[0]
        cur_len = 1
        moves = 0

        for i in range(1, len(s)):
            if s[i] != cur_bit:
                if cur_len % 2 != 0:
                    moves += 1
                else:
                    cur_len = 0
                    cur_bit = s[i]
            cur_len += 1
                
        return moves
        