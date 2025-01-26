//https://leetcode.com/problems/neighboring-bitwise-xor/?envType=daily-question&envId=2025-01-26
class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int total =0;

        for (int num : derived) {
            total ^= num;
        }
        return total == 0;
    }
}
