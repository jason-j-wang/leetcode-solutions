//https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/?envType=daily-question&envId=2025-09-13
class Solution {
    public int maxFreqSum(String s) {
        Map<Character, Integer> m = new HashMap<>();
        int con = 0;
        int vowel = 0;

        for (int i = 0; i < s.length(); i++) {
            char c= s.charAt(i);

            if (!m.containsKey(c)) {
                m.put(c, 0);
            }

            int count = m.get(c);
            m.put(c, ++count);

            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                if (count > vowel) {
                    vowel = count;
                }
            } else {
                if (count > con) {
                    con = count;
                }
            }
        }

        return con + vowel;
    }
}