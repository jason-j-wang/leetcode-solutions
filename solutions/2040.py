#https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/description/?envType=daily-question&envId=2025-06-25
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        left, right = -10 ** 10, 10 ** 10

        while left < right:
            mid = left + (right - left) // 2

            if self.solve(nums1, nums2, mid) < k:
                left = mid + 1
            else:
                right = mid
        return left


    def solve(self, nums1, nums2, target):
        count = 0
        n2 = len(nums2)

        for n in nums1:
            if n > 0:
                count += bisect.bisect_right(nums2, target // n)
            elif n < 0:
                t = target // n
                if target % n != 0:
                    t += 1
                count += len(nums2) - bisect.bisect_left(nums2, t)
            else:
                if target >= 0:
                    count += len(nums2)
        return count