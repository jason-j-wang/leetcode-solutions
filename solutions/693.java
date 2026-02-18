//https://leetcode.com/problems/binary-number-with-alternating-bits/description/?envType=daily-question&envId=2026-02-18
class Solution {
    public boolean hasAlternatingBits(int n) {
        boolean one = (n & 1) == 1;

        while (n != 0) {
            if (one && (n & 1) != 1) {
                return false;
            } else if (!one && (n & 1) != 0) {
                return false;
            }

            one = !one;
            n >>= 1;
        }
        return true;
    }
}