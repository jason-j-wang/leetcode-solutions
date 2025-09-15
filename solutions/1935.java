//https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=daily-question&envId=2025-09-15
class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        boolean[] broken = new boolean[26];

        for (int i = 0; i < brokenLetters.length(); i++) {
            broken[brokenLetters.charAt(i) - 'a'] = true;
        }

        String[] words = text.split(" ");
        int ans = words.length;

        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                if (broken[word.charAt(i) - 'a']) {
                    ans--;
                    break;
                }
            }
        }

        return ans;
    }
}