#https://leetcode.com/problems/reordered-power-of-2/description/?envType=daily-question&envId=2025-08-10
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if not (n & (n-1)):
            return True
        
        str_num = str(n)
        counts = Counter(str_num)

        p = 1

        while p < 10 ** 9:
            str_p = str(p)
            count_p = Counter(str_p)

            if len(counts) == len(count_p):
                valid = True

                for num in counts:
                    if counts[num] != count_p[num]:
                        valid = False
                        break

                if valid:
                    return True

            p *= 2
        return False