#https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/?envType=daily-question&envId=2025-06-14
class Solution:
    def minMaxDifference(self, num: int) -> int:
        exp = int(log(num)//log(10))
        max_replace = -1
        min_replace = -1
        max = 0
        min = 0
        
        for i in range(exp, -1, -1):
            n = num // (10 ** i)

            if (max_replace == -1 and n != 9) or n == max_replace:
                max_replace = n
                max += 9 * (10 ** i)

            else:
                max += n * (10 ** i)

            if (min_replace == -1 and n != 0) or n == min_replace:
                min_replace = n

            else:
                min += n * (10 ** i)

            num %= (10 ** i)

        return max - min

        