#https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append((nums[i], nums[j], nums[k]))
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return ans
                    
            