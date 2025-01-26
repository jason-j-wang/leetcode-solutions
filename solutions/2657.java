//https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/?envType=daily-question&envId=2025-01-26
class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int[] count = new int[A.length+1];
        int[] ans = new int[A.length];
        int cur_same = 0;
        for (int i =0; i < A.length; i++) {
            if (++count[A[i]] == 2) {
                cur_same++;
            }
            if (++count[B[i]] == 2) {
                cur_same++;
            }

            ans[i] = cur_same;

        }
        return ans;
    }
}
