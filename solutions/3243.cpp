//https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/?envType=daily-question&envId=2025-02-03
class Solution {
public:
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        
        vector<vector<int>> graph(n);

        for (int i = 0; i < n - 1; i++) {
            graph[i].push_back(i + 1);
        }

        vector<int> ans;

        for (auto query : queries) {
            vector<int> dist(n, INT_MAX);
            dist[0] = 0;

            graph[query[0]].push_back(query[1]);
            queue<int> q;
            q.push(0);

            while (q.size() != 0) {
                int node = q.front();
                q.pop();

                int d = dist[node] + 1;

                for (int n : graph[node]) {
                    if (d < dist[n]) {
                        dist[n] = d;
                        q.push(n);
                    }
                }
            }
            ans.push_back(dist[n-1]);
        }

        return ans;


    }
};