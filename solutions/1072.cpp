//https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/?envType=daily-question&envId=2025-02-03
class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        unordered_map<string, int> umap;

        for (int i = 0; i < matrix.size(); i++) {
            string key = "";
            for (int j = 0; j < matrix[0].size(); j++) {
                char c = matrix[i][j] == matrix[i][0] ? 'T' : 'F';
                key += c;
            }

            if (umap.find(key) == umap.end()) {
                umap[key] = 1;
            } else {
                umap[key] += 1;
            }
        }
        vector<int> values;
        for (auto pair : umap) {
            values.push_back(pair.second);
        }
        return *max_element(values.begin(), values.end());

    }
};