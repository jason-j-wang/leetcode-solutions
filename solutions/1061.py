#https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/?envType=daily-question&envId=2025-06-05
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]

        for i in range(len(s1)):
            a = s1[i]
            b = s2[i]

            parent_a = self.find(parent, ord(a) - ord('a'))
            parent_b = self.find(parent, ord(b) - ord('a'))

            if parent_a < parent_b:
                parent[parent_b] = parent_a
            else:
                parent[parent_a] = parent_b

        ans = ""
        for c in baseStr:
            ans += chr(self.find(parent, ord(c) - ord('a')) + ord('a'))

        return ans

    def find(self, parent, x):
        while parent[x] != x:
            x = parent[x]
        return parent[x]