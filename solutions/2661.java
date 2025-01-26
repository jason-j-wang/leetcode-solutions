//https://leetcode.com/problems/first-completely-painted-row-or-column/?envType=daily-question&envId=2025-01-26
class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;

        int [][] idx = new int[n * m + 1][2];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                idx[mat[i][j]][0] = i;
                idx[mat[i][j]][1] = j;
            }
        }

        int[] rows = new int[n];
        int[] cols = new int[m];

        for (int i = 0; i < arr.length; i++) {
            int num = arr[i];

            rows[idx[num][0]]++;
            cols[idx[num][1]]++;

            if (rows[idx[num][0]] == m || cols[idx[num][1]] == n) {
                return i;
            }
        }
        return arr.length-1;
    }
}
