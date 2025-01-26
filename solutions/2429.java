//https://leetcode.com/problems/minimize-xor/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public int minimizeXor(int num1, int num2) {
        int count = Integer.bitCount(num2);
        System.out.println(count);
        int[] bits = new int[32];

        int[] ans = new int[32];

        for (int i =0; i < 32; i++) {
            bits[i] = num1 & 1;
            num1 >>>= 1;
        }

        for (int i = 31; i >= 0; i--) {
            if (count <= 0) {
                break;
            }
            if (bits[i] == 1) {
                ans[i] = 1;
                count--;
            }
        }

        for (int i = 0; i < 32; i++) {
            if (count <= 0) {
                break;
            }
            if (bits[i] == 0) {
                ans[i] = 1;
                count--;
            }
        }

        int num = 0;
         for (int i = 31; i >= 0; i--) {
            num <<= 1;
            num |= ans[i];
        }

        return num;
    }
}