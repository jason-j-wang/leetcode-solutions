//https://leetcode.com/problems/permutations/submissions/757881499/
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> answer;
        solve(nums, 0, answer);
        
        return answer;
    }
    
    
    void solve(vector<int>& nums, int index, vector<vector<int>>& answer) {
        
        if (index == nums.size() - 1) {
            answer.push_back(nums);
            return;
        }
        
        for (int i = index; i < nums.size(); i++) {
            swap(nums[i], nums[index]);
            solve(nums, index + 1, answer);
            swap(nums[i], nums[index]);
        }
    }
        
};