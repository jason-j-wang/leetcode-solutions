//https://leetcode.com/problems/check-if-n-and-its-double-exist/?envType=daily-question&envId=2025-02-03
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int, int> umap;

        for (int n : arr) {
            if (umap[n * 2] > 0 || (n % 2 == 0 && umap[n / 2] > 0)) {
                return true;
            }
            umap[n]++;
        }


        return false;
    }
};