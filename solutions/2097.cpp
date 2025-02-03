//https://leetcode.com/problems/valid-arrangement-of-pairs/description/?envType=daily-question&envId=2025-02-03
class Solution {
public:
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        int n = pairs.size();
        unordered_map<int, queue<int>> adj;
        unordered_map<int, pair<int, int>> counts;

        vector<vector<int>> ans;
        vector<int> path;

        for (auto pair : pairs) {
            adj[pair[0]].push(pair[1]);
            counts[pair[0]].first++;
            counts[pair[1]].second++;
        }

        int start = -1;
        for (auto c : counts) {
           
            if (c.second.first > c.second.second) {
                start = c.first;
                break;
            }
        }

        if (start == -1) {
            start = pairs[0][0];
        }
        dfs(adj, start, path);

        reverse(path.begin(), path.end());

        for (int i = 1; i < path.size(); ++i) {
            ans.push_back({path[i - 1], path[i]});
        }

        return ans;
    }

    void dfs(unordered_map<int, queue<int>> &adj, int node, vector<int> &path) {
        while (!adj[node].empty()) {
            int next = adj[node].front();
            adj[node].pop();
            dfs(adj, next, path);
        }
        path.push_back(node);
       
    }
};