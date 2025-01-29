//https://leetcode.com/problems/redundant-connection/description/?envType=daily-question&envId=2025-01-29
class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int[] parent = new int[edges.length+1];
        int[] rank = new int[edges.length+1];

        for (int i = 0; i < edges.length+1;i++) {
            parent[i] = i;
            rank[i] = 1;
        }

        for (int[] e : edges) {
            if (!union(e[0], e[1], parent, rank)) {
                return e;
            }
        }
        return edges[0];
    }
    public int find(int x, int[] parent) {
        if (parent[x] != x) {
            parent[x] = find(parent[x], parent);
        }
        return parent[x];
    }

    public boolean union(int x, int y, int[] parent, int[] rank) {
        int rootX = find(x, parent);
        int rootY = find(y, parent);

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            return true;
        } else {
            return false;
        }
    }
}