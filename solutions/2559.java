//https://leetcode.com/problems/count-vowel-strings-in-ranges/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        int[] count = new int[words.length];
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

        if (vowels.contains(words[0].charAt(0)) && vowels.contains(words[0].charAt(words[0].length()-1))) {
            count[0] = 1;
        }

        for (int i = 1; i < words.length; i++) {
            count[i] = count[i-1];
            if (vowels.contains(words[i].charAt(0)) && vowels.contains(words[i].charAt(words[i].length()-1))) {
                count[i]++;
            }
        }

        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            if (queries[i][0] == 0) {
                ans[i] = count[queries[i][1]];
            } else {
                ans[i] = count[queries[i][1]] - count[queries[i][0]-1];
            }
        }
        return ans;
    }
}
