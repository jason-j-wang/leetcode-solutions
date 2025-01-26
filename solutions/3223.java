//https://leetcode.com/problems/minimum-length-of-string-after-operations/?envType=daily-question&envId=2025-01-26
class Solution {
    public int minimumLength(String s) {
        int[] counts = new int[26];

        for (int i = 0; i < s.length(); i++) {
            counts[s.charAt(i) - 'a']++;
        }
        int new_len = 0;
        for (int i = 0; i < counts.length; i++) {
            if (counts[i] > 0) {
                if (counts[i] % 2 == 0) {
                    new_len += 2;
                } else {
                    new_len++;
                }
            }
        }
        return new_len;
    }
}