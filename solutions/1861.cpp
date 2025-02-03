//https://leetcode.com/problems/rotating-the-box/?envType=daily-question&envId=2025-02-03
class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int n = box.size();
        int m = box[0].size();

        vector<vector<char>> new_box(m, vector<char>(n, '\0'));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                new_box[j][i] = box[i][j];
            }
        }

        for (int i = 0; i < m; i++) {
            reverse(new_box[i].begin(), new_box[i].end());
        }


        for (int i = 0; i < n; i++) {
            for (int j = m - 1; j > -1; j--) {
                if (new_box[j][i] == '#') {
                    int cur = j + 1;
                    while (cur < m && new_box[cur][i] == '.') {
                        swap(new_box[cur-1][i], new_box[cur][i]);
                        cur++;
                    }
                }
            }
        }
        return new_box;
    }
};