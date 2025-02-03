//https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/?envType=daily-question&envId=2025-02-03
class Solution {
    public int minSwaps(String s) {
        int ans = 0;
         for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[') {
                ans++;
            } else if (ans > 0) {
                ans--;
            }
         }
         return (ans + 1) / 2;
    }
}
