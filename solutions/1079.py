#https://leetcode.com/problems/letter-tile-possibilities/?envType=daily-question&envId=2025-02-17
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        counts = defaultdict(int)
        for t in tiles:
            counts[t] += 1
        self.build(counts, ans, "")
        return len(ans) -1

    def build(self, counts, ans, s):
        ans.add(s)

        for c in counts:
            if counts[c] > 0:
                counts[c] -= 1
                self.build(counts, ans, s + c)
                counts[c] += 1
        