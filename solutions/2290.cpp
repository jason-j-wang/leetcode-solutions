//https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/?envType=daily-question&envId=2025-02-03
class Solution {
public:
    int minimumObstacles(vector<vector<int>>& grid) {

        vector<vector<int>> directions = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> graph(m, vector<int>(n, INT_MAX));
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        
        graph[0][0] = grid[0][0];

        pq.push({graph[0][0], 0, 0});

        while (pq.size() != 0) {
            vector<int> node = pq.top();
            pq.pop();

            int removed = node[0];
            int i = node[1];
            int j = node[2];

            if (i == m - 1 && j == n - 1) {
                return removed;
            }

            for (auto d : directions) {
                int new_i = i + d[0];
                int new_j = j + d[1];

                if (new_i >= 0 && new_i < m && new_j >= 0 && new_j < n) {
                    int inc = grid[new_i][new_j];

                    if (removed + inc < graph[new_i][new_j]) {
                        pq.push({removed + inc, new_i, new_j});
                        graph[new_i][new_j] = removed + inc;
                    }
                }
            }
        }
        return -1;
    }
};