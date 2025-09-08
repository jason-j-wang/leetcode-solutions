//https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/?envType=daily-question&envId=2025-09-08
class Solution {
    public int[] getNoZeroIntegers(int n) {
        for (int i = 1; i < n / 2 + 1; i++) {
            if (!this.hasZero(i) && !this.hasZero(n - i)) {
                return new int[]{i, n - i};
            }
        }
        return new int[]{};
    }

    private boolean hasZero(int n) {
        while (n != 0) {
            if (n % 10 == 0) {
                return true;
            }
            n /= 10;
        }
        return false;
    }
}
