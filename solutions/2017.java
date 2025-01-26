//https://leetcode.com/problems/grid-game/?envType=daily-question&envId=2025-01-26
class Solution {
    public long gridGame(int[][] grid) {
        int m = grid[0].length;

        long row1 = 0;
        for (int num : grid[0]) {
            row1 += num;
        }
        
        long row2 = 0;
        long minSum = Long.MAX_VALUE;

        for (int i = 0; i < m; i++) {
            row1 -= grid[0][i];
            
            minSum = Math.min(minSum, Math.max(row1, row2));
            row2 += grid[1][i];
        }
        return minSum;
    }

}
