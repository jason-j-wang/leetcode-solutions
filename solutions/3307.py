#https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/submissions/1685598556/?envType=daily-question&envId=2025-07-04
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        num_transfs = 0
        cur_exp = ceil(log(k)/log(2))

        while k != 1:
            
            while 2 ** cur_exp >= k:
                cur_exp -= 1
            k -= 2 ** cur_exp
            if operations[cur_exp] == 1:
                num_transfs += 1
            
            

        return chr(ord('a') + (num_transfs % 26))