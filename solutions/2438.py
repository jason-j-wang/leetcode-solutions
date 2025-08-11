#https://leetcode.com/problems/range-product-queries-of-powers/description/?envType=daily-question&envId=2025-08-11
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        exps = []
        exp = 0
        mod = 10 ** 9 + 7
        while n > 0:
            
            if n & 1:
                exps.append(exp)
            exp += 1
            n >>= 1
        prefix = [0 for _ in range(len(exps))]
        prefix[0] = exps[0]
        for i in range(1, len(exps)):
            prefix[i] = (exps[i] + prefix[i-1])
        ans = []
        

        for left, right in queries:
            if left != right:
                sub = prefix[left - 1] if left >= 1 else 0
                ans.append((2 ** (prefix[right] - sub)) % mod)
            else:
                ans.append(2 ** exps[left])
        return ans
