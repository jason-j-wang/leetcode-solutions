//https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public int maxScore(String s) {
        int score = (s.charAt(0) == '0') ? 1 : 0;

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                score++;
            }
        }

        int ans = score;

        for (int i = 1; i < s.length()-1; i++) {
            if (s.charAt(i) == '0') {
                score++;
            } else {
                score--;
            }
            ans = Math.max(ans, score);
        }
        return ans;
    }
}
