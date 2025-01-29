//https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=top-interview-150
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int n : nums) {
            ans ^= n;
        }
        return ans;
    }
}