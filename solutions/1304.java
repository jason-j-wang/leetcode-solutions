//https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/?envType=daily-question&envId=2025-09-07
class Solution {
    public int[] sumZero(int n) {
        int[] ans = new int[n];
        int cur = 1;
        for (int i = n % 2 == 0 ? 0 : 1; i < n; i += 2) {
            ans[i] = cur;
            ans[i+1] = -cur;
            cur++;
        }
        return ans;
    }
}