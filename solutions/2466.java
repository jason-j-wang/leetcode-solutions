//https://leetcode.com/problems/count-ways-to-build-good-strings/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public int countGoodStrings(int low, int high, int zero, int one) {
        int mod = (int) Math.pow(10, 9) + 7;

        int[] dp = new int[high+1];
        dp[0] = 1;

        for (int i = 1; i <= high; i++) {
            if (i - zero >= 0) {
                
                dp[i] += dp[i-zero];
            }

            if (i - one >= 0) {
                
                dp[i] += dp[i-one];
            }

            dp[i] %= mod;
            
        }
        int ans = 0;
        for (int i = low; i <=high; i++) {
            ans += dp[i];
            ans %= mod;
        }
        return ans;
    }
}
