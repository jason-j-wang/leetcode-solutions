//https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2025-02-03
class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long total = 0;

        int num_negs = 0;

        int min_num = INT_MAX;

        for (int i = 0 ; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                int num = matrix[i][j];
                int abs_num = abs(matrix[i][j]);

                if (num < 0) {
                    num_negs++;
                }

                total += abs_num;
                min_num = min(min_num, abs_num);
            }
        }

        if (num_negs % 2 == 0) {
            return total;
        }

        return total - min_num * 2;
    }
};