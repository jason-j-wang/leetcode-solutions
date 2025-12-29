#https://leetcode.com/problems/pyramid-transition-matrix/?envType=daily-question&envId=2025-12-29
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        m = defaultdict(list)

        for a in allowed:
            m[a[0] + a[1]].append(a[2])

        dp = defaultdict(bool)

        def solve(base):
            if len(base) == 1:
                return True

            if base in dp:
                return dp[base]

            next_layer = []
            build_all(base, 0, next_layer, [])

            for layer in next_layer:
                if solve(layer):
                    dp[layer] = True
                    return True
                dp[layer] = False
            
            dp[base] = False
            return False

            
        def build_all(base, i, res, cur):
            if i >= len(base) - 1:
                return

            if base[i] + base[i+1] not in m:
                return

            for c in m[base[i] + base[i+1]]:
                cur.append(c)
                if len(cur) == len(base) - 1:
                    res.append("".join(cur))
                else:
                    build_all(base, i + 1, res, cur)

                cur.pop()
            
        return solve(bottom)

            