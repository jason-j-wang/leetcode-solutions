//https://leetcode.com/problems/defuse-the-bomb/?envType=daily-question&envId=2025-02-03
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        vector<int> ans(code.size());

        if (k == 0){
            return ans;
        }

        if (k > 0) {
            for (int i = 0; i < code.size(); i++) {
                int s = 0;
                for (int j = i+1; j < i + k + 1; j++) {
                    s = s + code[j % code.size()];
                }
                ans[i] = s;
            }
            return ans;
        }

        for (int i = 0; i < code.size(); i++) {
            int s = 0;
            for (int j = i - 1; j > i + k - 1; j--) {
                s = s + code[(j  + code.size()) % code.size()];
                cout << j << code.size() << endl;
                cout << j % code.size() << endl;
            //cout << (j  + code.size()) % code.size() << endl;
            }
            ans[i] = s;
        }
        return ans;
    }
};