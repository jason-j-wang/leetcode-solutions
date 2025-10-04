//https://leetcode.com/problems/container-with-most-water/?envType=daily-question&envId=2025-10-04
class Solution {
    public int maxArea(int[] height) {
        int ans = 0;

        int l = 0, r = height.length - 1;

        while (l < r) {
            ans = Math.max(ans, Math.min(height[l], height[r]) * (r - l));
            if (height[r] < height[l]) {
                r--;
            } else {
                l++;
            }
        }
        return ans;
    }
}