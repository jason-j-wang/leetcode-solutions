//https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2025-09-21
class Solution {
    public int maxFrequencyElements(int[] nums) {
        int[] counts = new int[101];

        int ans = 0;
        int max = 0;
        for (int n : nums) {
            int c = ++counts[n];

            if (c == max) {
                ans += c;
            } else if (c > max) {
                ans = c;
                max = c;
            }
        }

        return ans;
    }
}