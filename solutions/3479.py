#https://leetcode.com/problems/fruits-into-baskets-iii/description/
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        sg = SegTree(baskets)
        ans = 0
        for f in fruits:
            i = sg.find(f)

            if i == -1:
                ans += 1
            else:
                sg.update(i, 0)
        return ans

class SegTree:
    def __init__(self, baskets):
        l = len(baskets)
        self.n = 2 ** ((l-1).bit_length())
        self.nodes = [0] * (self.n * 2)

        for i, f in enumerate(baskets):
            self.update(i + self.n, f)

    def update(self, i, val):
        self.nodes[i] = val

        while i > 1:
            i //= 2
            self.nodes[i] = max(self.nodes[i * 2], self.nodes[i * 2 + 1])

    def find(self, target):
        if self.nodes[1] < target:
            return -1

        i = 1

        while i < self.n:
            if self.nodes[i * 2] >= target:
                i *= 2
            else:
                i = i * 2 + 1
        return i