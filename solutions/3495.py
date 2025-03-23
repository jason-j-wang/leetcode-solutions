#https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        total = 0
        for l, r in queries:
            cur = 0
            lower = log(l)//log(4) + 1
            upper = log(r)//log(4) + 1


            if lower == upper:
                cur += lower * (r - l + 1)
                total += cur // 2

                if cur % 2 == 1:
                    total += 1
            else:
                p = lower
                while p != upper + 1:
                    if p == lower:
                        cur += p * (4 ** p - l)
                    elif p == upper:
                        cur += p * (r - 4 ** (p-1) + 1)
                    else:
                        cur += p * (4 ** p - 4 ** (p-1))
                    p += 1
                
                total += cur // 2

                if cur % 2 == 1:
                    total += 1
        return int(total)
