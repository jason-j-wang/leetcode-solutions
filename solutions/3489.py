#https://leetcode.com/problems/zero-array-transformation-iv/
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        prefix = [[] for i in range(len(nums))]
        mem = defaultdict(list)
        for i in range(len(queries)+1):
            if i != 0:
                left, right, val = queries[i-1]
                prefix[left].append(val)
                if right + 1 < len(prefix):
                    prefix[right + 1].append(-val)
            if self.validate(queries, i, prefix, nums, mem):
                return i

        return -1

    def validate(self, queries, k, prefix, nums, mem):
        num_counts = defaultdict(int)
        
        for i in range(len(nums)):
            poss = set([0])
            for p in prefix[i]:
                if p > 0:
                    num_counts[p] += 1
                else:
                    num_counts[-p] -= 1
            arr = []
            for n in num_counts:
                for j in range(num_counts[n]):
                    arr.append(n)
            
            for n in num_counts:
                adds = set()
                for x in range(num_counts[n]):
                    if (x + 1) * n <= nums[i]:
                        adds.add((x + 1) * n)
                b = set(adds)
                for z in poss:
                    for a in adds:
                        if z + a <=  nums[i]:
                            b.add(z + a)
                poss |= b

            if nums[i] not in poss:
                return False
        return True
