//https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/?envType=daily-question&envId=2025-02-03

class Solution {
    public int minAddToMakeValid(String s) {
        int left = 0;
        int unmatched = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                left++;
            } else if (s.charAt(i) == ')') {
                if (left > 0) {
                    left--;
                } else {
                    unmatched++;
                }
            }
        }
        return unmatched + left;
    }
}