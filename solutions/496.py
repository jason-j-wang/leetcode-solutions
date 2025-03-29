#https://leetcode.com/problems/next-greater-element-i/description/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapped = {}
        nextge = []
        for i in range(len(nums2)-1, -1, -1):
            n = nums2[i]
            mapped[n] = i

            while stack and nums2[stack[-1]] < n:
                stack.pop()

            if not stack:
                nextge.append(-1)
            else:
                nextge.append(nums2[stack[-1]])
            stack.append(i)

        nextge.reverse()

        ans = [nextge[mapped[n]] for n in nums1]
        return ans