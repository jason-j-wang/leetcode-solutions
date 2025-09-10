//https://leetcode.com/problems/minimum-number-of-people-to-teach/description/?envType=daily-question&envId=2025-09-10
class Solution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        int maxLang = 0;
        
        Set<Integer> taught = new HashSet<>();

        Map<Integer, Set<Integer>> languageMap = new HashMap<>();

        for (int i = 0; i < languages.length; i++) {
            Set<Integer> s = new HashSet<>();
            for (int lang : languages[i]) {
                s.add(lang);

                if (lang > maxLang) {
                    maxLang = lang;
                }
            }
            languageMap.put(i + 1, s);
        }

        int[] knowPerLanguage = new int[maxLang + 1];
        knowPerLanguage[0] = 0;

        for (int i = 0; i < friendships.length; i++) {
            Set<Integer> intersection = new HashSet<>();
            Set<Integer> setA = languageMap.get(friendships[i][0]);
            Set<Integer> setB = languageMap.get(friendships[i][1]);
            intersection.addAll(setA);
            intersection.retainAll(setB);

            if (intersection.size() == 0) {
                
                if (!taught.contains(friendships[i][0])) {
                    for (int lang : setA) {
                        knowPerLanguage[lang]++;
                    }
                }

                 if (!taught.contains(friendships[i][1])) {
                    for (int lang : setB) {
                        knowPerLanguage[lang]++;
                    }
                }
                taught.add(friendships[i][0]);
                taught.add(friendships[i][1]);
            }
        }

        int t = taught.size();
        int ans = t;

        for (int num : knowPerLanguage) {
            if (t - num < ans) {
                ans = t - num;
            }
        }
        return ans;
    }
}