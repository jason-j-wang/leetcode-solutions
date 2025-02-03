//https://leetcode.com/problems/find-champion-ii/description/?envType=daily-question&envId=2025-02-03
class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {

        unordered_map<int, vector<int>> graph;
        for (auto e : edges) {
            graph[e[1]].push_back(e[0]);
            
        }

        int single = -1;

        for (int i =0; i < n; i++) {
            if (graph[i].size() == 0 && single != -1) {
                return -1;
            }

            if (graph[i].size() == 0) {
                single = i;
            }
        }
        return single;
    }
};