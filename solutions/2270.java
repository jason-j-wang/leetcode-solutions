//https://leetcode.com/problems/number-of-ways-to-split-array/?envType=daily-question&envId=2025-01-26
class Solution {
    public int waysToSplitArray(int[] nums) {

        long totalPosSum = 0;
        long totalNegSum = 0;
        for (int n : nums) {
            if (n > 0) {
                totalPosSum += n;
            } else {
                totalNegSum += n;
            }
        }

        int ans = 0;
        long curSum = 0;

        for (int i =0; i < nums.length; i++) {
            curSum += nums[i];

            if (nums[i]>0) {
                totalPosSum -= nums[i];
            } else {
                totalNegSum -= nums[i];
            }

            if (curSum >= totalPosSum + totalNegSum && i < nums.length-1) {
                ans++;
            }
        }
        return ans;

        
    }
}
