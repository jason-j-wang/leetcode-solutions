//https://leetcode.com/problems/add-binary/description/?envType=daily-question&envId=2026-02-15
class Solution {
    public String addBinary(String a, String b) {
        int lenA = a.length();
        int lenB = b.length();
        int len = Math.max(lenA, lenB);

        int carry = 0;
        char[] ans = new char[len + 1];

        for (int i = 0; i < len; i++) {
            int aIdx = lenA - 1 - i;
            int bIdx = lenB - 1 - i;

            int aBit = aIdx >= 0 ? a.charAt(aIdx) - '0' : 0;
            int bBit = bIdx >= 0 ? b.charAt(bIdx) - '0' : 0;

            int num = aBit + bBit + carry;
            carry = num / 2;

            ans[len - i] = (char) ('0' + (num % 2));
        }

        if (carry == 1) {
            ans[0] = '1';
            return new String(ans);
        }

        return new String(ans, 1, len);
    }
}
