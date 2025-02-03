//https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/?envType=daily-question&envId=2025-02-03
class Solution {
public:
    int minimumTime(vector<vector<int>>& grid) {
        if (grid[0][1] > 1 && grid[1][0] > 1) {
            return -1;
        }
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        vector<vector<bool>> visited(m, vector<bool>(n, false));

        priority_queue<vector<int>, vector<vector<int>>, greater<>> pq;
        pq.push({grid[0][0], 0, 0});

        while (!pq.empty()) {
            auto cur = pq.top();
            pq.pop();
            int time = cur[0];
            int i = cur[1];
            int j = cur[2];

            if (i == m - 1 && j == n - 1) {
                return time;
            }

            if (visited[i][j]) {
                continue;
            }
            visited[i][j] = true;

            for (auto d : directions) {
                int new_i = i + d[0];
                int new_j = j + d[1];
                
                if (new_i >= 0 && new_i < m && new_j >= 0 && new_j < n && !visited[new_i][new_j]) {
                    int wait_time = ((grid[new_i][new_j] - time) % 2 == 0) ? 1 : 0;
                    int next_time = max(grid[new_i][new_j] + wait_time, time + 1);
                    pq.push({next_time, new_i, new_j});
                }
                
            }
        }
        return -1;
    }

};