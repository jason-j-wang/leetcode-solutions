#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c = nums1[0:m]

        ans_ptr = 0
        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if c[p1] < nums2[p2]:
                nums1[ans_ptr] = c[p1]
                p1 += 1
            else:
                nums1[ans_ptr] = nums2[p2]
                p2 += 1
            ans_ptr += 1

        while ans_ptr < n + m:
            if p1 < m:
                nums1[ans_ptr] = c[p1]
                p1 += 1
            else:
                nums1[ans_ptr] = nums2[p2]
                p2 += 1
            ans_ptr += 1
        
        