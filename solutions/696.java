//https://leetcode.com/problems/count-binary-substrings/description/?envType=daily-question&envId=2026-02-19
class Solution {
    public int countBinarySubstrings(String s) {
        int ans = 0;
        int prev = 0;
        int cur = 1;

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) != s.charAt(i-1)) {
                ans += Math.min(prev, cur);
                prev = cur;
                cur = 1;
            } else {
                cur += 1;
            }
        }

        ans += Math.min(prev, cur);
        return ans;
    }
}