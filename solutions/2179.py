#https://leetcode.com/problems/count-good-triplets-in-an-array/
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        mapped = {}
        for i, n in enumerate(nums1):
            mapped[n] = i

        n = len(nums2)
        ans = 0
        ordered_set = []

        for v in nums2:
            i = mapped[v]
            nums_smaller = bisect.bisect_left(ordered_set, i)
            nums_larger = (n - 1 - i) - (len(ordered_set) - nums_smaller)
            ans += nums_smaller * nums_larger
            bisect.insort(ordered_set, i)
        return ans