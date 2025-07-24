#https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/?envType=daily-question&envId=2025-07-24
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        subtree_xor = [0] * n
        descendants = [set() for _ in range(n)]

        def dfs(node, parent):
            subtree_xor[node] = nums[node]
            descendants[node].add(node)
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    subtree_xor[node] ^= subtree_xor[neighbor]
                    descendants[node].update(descendants[neighbor])
        dfs(0, -1)
        
        total_xor = subtree_xor[0]
        min_score = float('inf')

        for i in range(1, n):
            for j in range(i + 1, n):
                xor_i = subtree_xor[i]
                xor_j = subtree_xor[j]
                
                # Case 1: j's subtree is inside i's subtree 
                if j in descendants[i]:
                    val1 = xor_j
                    val2 = xor_i ^ xor_j
                    val3 = total_xor ^ xor_i
                
                # Case 2: i's subtree is inside j's subtree 
                elif i in descendants[j]:
                    val1 = xor_i
                    val2 = xor_j ^ xor_i
                    val3 = total_xor ^ xor_j

                # Case 3: i and j are in independent branches
                else:
                    val1 = xor_i
                    val2 = xor_j
                    val3 = total_xor ^ xor_i ^ xor_j

                score = max(val1, val2, val3) - min(val1, val2, val3)
                min_score = min(min_score, score)
                
        return min_score

