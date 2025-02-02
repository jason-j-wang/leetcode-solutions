#https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        return max(self.traverse(s, True, True, k), self.traverse(s, True, False, k), self.traverse(s, False, True, k), self.traverse(s, False, False, k))

    def traverse(self, s, north, west, k):
        pos = [0, 0]
        ans = 0
        for c in s:
            #print(count)
            if c == 'N':
                if not north and k > 0:
                    k -= 1
                    pos[0] -= 1
                else:
                    pos[0] += 1
            elif c == 'S':
                if north and k > 0:
                    pos[0] += 1
                    k -= 1
                else:
                    pos[0] -= 1
            elif c == 'W':
                if not west and k > 0:
                    k -= 1
                    pos[1] += 1
                else:
                    pos[1] -= 1
            else:
                if west and k > 0:
                    pos[1] -= 1
                    k -= 1
                else:
                    pos[1] += 1
            ans = max(ans, abs(pos[0]) + abs(pos[1]))
        return ans