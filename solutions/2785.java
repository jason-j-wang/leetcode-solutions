//https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2025-09-11
class Solution {
    public String sortVowels(String s) {
        Character[] arr = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'};
        Set<Character> vowels = new HashSet<>(Arrays.asList(arr));

        Map<Character, Integer> m = new HashMap<>();

        for (Character c : arr) {
            m.put(c, 0);
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (vowels.contains(c)) {
                int num = m.get(c);
                m.put(c, num + 1);
            }
        }

        int ptr = 0;
        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (vowels.contains(c)) {
                char v = arr[ptr];
                int numLeft = m.get(v);
                while (numLeft == 0) {
                    ptr++;
                    v = arr[ptr];
                    numLeft = m.get(v);
                }

                ans.append(v);
                m.put(v, numLeft - 1);

                
            } else {
                ans.append(c);
            }
        }

        return ans.toString();
    }
}