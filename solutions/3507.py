#https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0

        arr = nums
        while not self.is_sorted(arr):
            ans += 1
            min_idx = 0
            min_pair = float("inf")
            for i in range(len(arr)-1):
                if arr[i] + arr[i+1] < min_pair:
                    min_idx = i
                    min_pair = arr[i] + arr[i+1]

            arr = arr[:min_idx] + [min_pair] + arr[min_idx+2:]
        return ans


    def is_sorted(self, arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True