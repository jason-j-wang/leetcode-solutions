//https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/?envType=daily-question&envId=2025-10-13
class Solution {
    public List<String> removeAnagrams(String[] words) {
        List<String> ans = new ArrayList<>();
        ans.add(words[0]);

        Map<Character, Integer> prevCount = new HashMap<>();

        for (int i = 0; i < words[0].length(); i++) {
            char c = words[0].charAt(i);

            prevCount.put(c, prevCount.getOrDefault(c, 0) + 1);
        }

        for (int i = 1; i < words.length; i++) {
            Map<Character, Integer> curCount = new HashMap<>();
            for (int j = 0; j < words[i].length(); j++) {
                char c = words[i].charAt(j);

                curCount.put(c, curCount.getOrDefault(c, 0) + 1);
            }

            if (!isEquals(prevCount, curCount)) {
                ans.add(words[i]);
            }

            prevCount = curCount;
        }

        return ans;
    }

    private boolean isEquals(Map<Character, Integer> word1, Map<Character, Integer> word2) {
        if (word1.size() != word2.size()) {
            return false;
        }

        for (char c : word1.keySet()) {
            if (!word2.containsKey(c) || word1.get(c) != word2.get(c)) {
                return false;
            }
        }

        return true;
    }
}