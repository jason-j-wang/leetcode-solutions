//https://leetcode.com/problems/construct-k-palindrome-strings/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public boolean canConstruct(String s, int k) {
        Map<Character, Integer> count = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (count.get(c) == null) {
                count.put(c, 1);
            } else {
                count.put(c, count.get(c) + 1);
            }
        }

        int num_odd =0;

        for (Character c : count.keySet()) {
            if (count.get(c) % 2 == 1) {
                num_odd++;
            }
        }
        return num_odd <= k && s.length() >= k;
    }
}
