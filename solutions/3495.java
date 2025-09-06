//https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/description/?envType=daily-question&envId=2025-09-06
class Solution {
    public long minOperations(int[][] queries) {
        long ans = 0;

        for (int i = 0; i < queries.length; i++) {
            int left = queries[i][0];
            int right = queries[i][1];

            int left_exp = (int) Math.floor(Math.log(left)/Math.log(4));
            int right_exp = (int) Math.floor(Math.log(right)/Math.log(4));
            
            long ops = 0;
            if (left_exp == right_exp) {
                long total = (long) (left_exp + 1) * (right - left + 1);

                ops += (total + 1) / 2;
                ans += ops;
            } else {
                long left_total = (left_exp + 1) * (long) (Math.pow(4, left_exp + 1) - left);
   

                for (int lower = left_exp + 1; lower < right_exp; lower++) {
                    long mid_total = (lower + 1) * (long) (Math.pow(4, lower + 1) - Math.pow(4, lower));
                    ops += mid_total;
                }

                long right_total = (right_exp + 1) * (long) (right - Math.pow(4, right_exp) + 1);
                ops += (left_total + right_total);

                ans += (ops + 1) / 2;
            }
        }
        return ans;
    }
}