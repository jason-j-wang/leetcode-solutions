//https://leetcode.com/problems/counting-words-with-a-given-prefix/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public int prefixCount(String[] words, String pref) {
        int ans = 0;
        int len = pref.length();
        for (String w : words) {
            if (w.length() >= len && w.substring(0, len).equals(pref)) {
                ans++;
            }
        }
        return ans;
    }
}
