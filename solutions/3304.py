#https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/?envType=daily-question&envId=2025-07-03
class Solution:
    def kthCharacter(self, k: int) -> str:
        num_transfs = 0
        cur_len = 2 ** ceil(log(k)/log(2))

        while k != 1:
            
            while cur_len >= k:
                cur_len //= 2
            k -= cur_len
  
            num_transfs += 1

        return chr(ord('a') + num_transfs)