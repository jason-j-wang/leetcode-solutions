#https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/submissions/1667738665/?envType=daily-question&envId=2025-06-18
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(0, len(nums), 3):
            arr = [nums[i], nums[i+1], nums[i+2]]

            if max(arr) - min(arr) <= k:
                ans.append(arr)
            else:
                return []
        return ans

