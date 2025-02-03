//https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/?envType=daily-question&envId=2025-02-03

class Solution {
    public boolean canArrange(int[] arr, int k) {
        
        int[] count = new int[k];
        
        for (int i : arr) {
            i %= k;
            if (i < 0) {
                i += k;
            }
            
            count[i]++;
        }

        if (k % 2 == 0 && count[k/2] % 2 != 0) {
            return false;
        }

        if (count[0] % 2 != 0) {
            return false;
        }

        for (int i = 1; i < k; i++) {
            if (count[i] != count[k - i]) {
                return false;
            }
        }

        return true;
    }
}