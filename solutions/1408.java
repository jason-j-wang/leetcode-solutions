//https://leetcode.com/problems/string-matching-in-an-array/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public List<String> stringMatching(String[] words) {
        List<String> ans = new ArrayList<>();
        boolean added = false;
        for (String word : words) {
            for (String match : words) {
                if (word.length() <= match.length() && !word.equals(match)) {
                    for (int i = 0; i < match.length()-word.length()+1; i++) {
                        if (match.substring(i, i+word.length()).equals(word)) {
                            ans.add(word);
                            added = true;
                            break;
                        }
                    }
                } 
                if (added) {
                    added = false;
                    break;
                }           
            }
        }
        return ans;

    }
}