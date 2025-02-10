#https://leetcode.com/problems/unique-binary-search-trees/description/?envType=problem-list-v2&envId=binary-tree
class Solution:
    def numTrees(self, n: int) -> int:
        mem = [0 for i in range(n+1)]

        mem[0] = 1
        
        for num_nodes in range(1, n+1):
            num_unique = 0
            for root_node_value in range(num_nodes+1):
                num_left_nodes = root_node_value - 1
                num_right_nodes = num_nodes - root_node_value

                num_unique += mem[num_left_nodes] * mem[num_right_nodes]
            mem[num_nodes] = num_unique

        return mem[n]

