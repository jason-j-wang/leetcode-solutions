#https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counts = []

        all_zeros = False
 
        while (not all_zeros):
            all_zeros = True
            cur_count = 0
            for i in range(len(candidates)):
                if candidates[i] != 0:
                    all_zeros = False
                   

                if candidates[i] % 2 == 1:
                    cur_count += 1

                candidates[i] = candidates[i] >> 1

            counts.append(cur_count)
   
        return max(counts)
