#https://leetcode.com/problems/container-with-most-water/?envType=problem-list-v2&envId=greedy
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height)-1

        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                if height[left+1] < height[right-1]:
                    right -= 1
                else:
                    left += 1

        return ans
        