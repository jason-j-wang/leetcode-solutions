//https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public boolean canBeValid(String s, String locked) {
        if (s.length() % 2 == 1) {
            return false;
        }

        Stack<Integer> opening = new Stack<>();
        Stack<Integer> wildcard = new Stack<>();

        for (int i =0; i < s.length(); i++) {
            if (locked.charAt(i) == '0') {
                wildcard.push(i);
            } else if (s.charAt(i) == '(') {
                opening.push(i);
            } else {
                if (!opening.empty()) {
                    opening.pop();
                } else if (!wildcard.empty()) {
                    wildcard.pop();
                } else {
                    return false;
                }
            }
        }

        while (!opening.empty()) {
            if (wildcard.empty()) {
                return false;
            }

            if (opening.peek() > wildcard.peek()) {
                return false;
            }

            opening.pop();
            wildcard.pop();
        }

        return true;


    }
}