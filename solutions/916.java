//https://leetcode.com/problems/word-subsets/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        Map<Character, Integer> totalRequired = new HashMap<>();
        Map<Character, Integer> required;

        for (String word : words2) {
            required = new HashMap<>();
            for (int i = 0; i < word.length(); i++) {
                if (!required.containsKey(word.charAt(i))) {
                    required.put(word.charAt(i), 1);
                } else {
                    required.put(word.charAt(i), required.get(word.charAt(i)) + 1);
                }
            }
            for (Character c : required.keySet()) {
                if (totalRequired.get(c) == null || totalRequired.get(c) < required.get(c)) {
                    totalRequired.put(c, required.get(c));
                }
            }
        }

        List<String> ans = new ArrayList<>();
        Map<Character, Integer> curWord;
        for (String word : words1) {
            curWord = new HashMap<>();
            for (int i = 0; i < word.length(); i++) {
                if (!curWord.containsKey(word.charAt(i))) {
                    curWord.put(word.charAt(i), 1);
                } else {
                    curWord.put(word.charAt(i), curWord.get(word.charAt(i)) + 1);
                }
            }
            boolean valid = true;
            for (Character c : totalRequired.keySet()) {
                if (curWord.get(c) == null || curWord.get(c) < totalRequired.get(c)) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                ans.add(word);
            }
            
        }
        return ans;
    }
}