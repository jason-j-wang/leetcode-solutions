#https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/description/
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # the moment we are foced to use a char that is >  than the target index, 
        # all remaining should be used in sorted order
        n = len(s)
        c = list(s)
        c.sort()

        used = [False for _ in range(n)]

        check = list(s)
        check.sort(reverse=True)
        if "".join(check) <= target:
            return ""

        mem = {}

        def solve(used, cur, idx, strict):
            st = "".join(cur)
            if st in mem:
                return mem[st]

            if idx == n:

                return st

            if not strict:
                rem = []
                for i in range(n):
                    if not used[i]:
                        rem.append(c[i])
                return st + "".join(rem)
    
            for i in range(n):
                if not used[i] and strict and c[i] >= target[idx]:
                    cur.append(c[i])
                    used[i] = True
                    stric = c[i] == target[idx]
                    ret = solve(used, cur, idx + 1, stric)

                    
                    if ret != None and ret != target:
                        mem[st] = ret
                        return ret
                        
                    cur.pop()
                    used[i] = False
            # no valid sol found
            mem[st] = None
            return None

        return solve(used, [], 0, True)