#https://leetcode.com/problems/partition-labels/description/?envType=daily-question&envId=2025-03-30
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        n = len(s)
        for i in range(n):
            last[s[i]] = i

        ans = []
        last_end = 0
        cur_right = 0

        for i in range(n):
            cur_right = max(cur_right, last[s[i]])

            if cur_right == i:
                ans.append(i - last_end + 1)
                last_end = cur_right + 1

        return ans