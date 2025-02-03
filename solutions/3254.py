#https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/?envType=daily-question&envId=2025-02-03
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        left = 0
        right = k-1
        n = len(nums)
        is_sorted = False
        up_to = -1
        ans = []

        while left < n - k + 1:
            #print("left", right)
            if is_sorted:
                #print(1)
                if nums[right] == nums[right - 1] + 1:
                    ans.append(nums[right])
                else:
                    is_sorted = False
                    ans.append(-1)
               
            elif up_to >= 0 and left <= up_to:
                #print(2)
                ans.append(-1)
              
            else:
                is_sorted = True
                #print(3)
                cur = left
                for i in range(1, k):
                    
                    if nums[cur+i] != nums[cur + i-1] + 1:
                        is_sorted = False
                        up_to = cur + i - 1
                        
                        break
                
                if is_sorted:
                    ans.append(nums[right])
                else:
                    ans.append(-1)

            left += 1
            right += 1
        return ans
            