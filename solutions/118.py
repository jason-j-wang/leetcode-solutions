#https://leetcode.com/problems/pascals-triangle/description/?envType=daily-question&envId=2025-08-01
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for i in range(1, numRows):
            row = [1]
            prev = ans[i-1]
            for j in range(1, len(prev)):
                row.append(prev[j-1] + prev[j])
            row.append(1)
            ans.append(row)
        return ans