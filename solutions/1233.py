#https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/?envType=daily-question&envId=2025-02-03
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]

        for i in range(1, len(folder)):

            if folder[i].startswith(ans[-1] + "/"):
                continue
            else:
                ans.append(folder[i])
        return ans
        