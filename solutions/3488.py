#https://leetcode.com/problems/closest-equal-element-queries/
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        num_map = defaultdict(list)
        idx_map = {}

        n = len(nums)
        for i in range(n):
            num_map[nums[i]].append(i)
            idx_map[i] = len(num_map[nums[i]]) - 1
            
        ans = []
        for q in queries:
            query_num = nums[q]
            query_list = num_map[query_num]
            length = len(query_list)
            if length == 1:
                ans.append(-1)
            else:
                q_idx = idx_map[q]
                before = 0
                after = 0
                if q_idx == 0:
                    before = length - 1
                    after = 1
                elif q_idx == length - 1:
                    before = length - 2
                    after = 0
                else:
                    before = q_idx - 1
                    after = q_idx + 1

                before_diff = query_list[q_idx] - query_list[before] if before < q_idx else query_list[q_idx] + n - query_list[before]
                after_diff = query_list[after] - query_list[q_idx] if after > q_idx else query_list[after] + n - query_list[q_idx]
                ans.append(min(before_diff, after_diff))
        return ans
                
        