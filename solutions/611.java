//https://leetcode.com/problems/valid-triangle-number/description/?envType=daily-question&envId=2025-09-26
class Solution {
    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        int ans = 0;

        for (int i = 0; i < nums.length; i++) {
            int k = i + 2;
            for (int j = i+1; j < nums.length; j++) {
                while (k < nums.length && nums[k] < nums[i] + nums[j]) {
                    k++;
                }
                if (k > j) {
                    ans += k - j - 1;
                }
                
            }
        }
        return ans;
    }
}