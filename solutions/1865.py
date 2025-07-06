#https://leetcode.com/problems/finding-pairs-with-a-certain-sum/description/?envType=daily-question&envId=2025-07-06
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts1 = defaultdict(int, Counter(nums1))
        self.counts2 = defaultdict(int, Counter(nums2))
        

    def add(self, index: int, val: int) -> None:
        self.counts2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counts2[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        ans = 0
        for n1 in self.counts1:
            if tot - n1 < 1:
                continue
            if tot - n1 in self.counts2:
                ans += self.counts1[n1] * self.counts2[tot-n1]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)