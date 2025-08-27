//https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/?envType=daily-question&envId=2025-08-27
class Solution {
    private static final int[][] DIRS = {
        { 1, 1 },
        { 1, -1 },
        { -1, -1 },
        { -1, 1 },
    };
    private int[][][][] memo;
    private int[][] grid;
    private int m, n;

    public int lenOfVDiagonal(int[][] grid) {
        this.grid = grid;
        this.m = grid.length;
        this.n = grid[0].length;
        this.memo = new int[m][n][4][2];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < 4; k++) {
                    Arrays.fill(memo[i][j][k], -1);
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    for (int direction = 0; direction < 4; direction++) {
                        ans = Math.max(ans, dfs(i, j, direction, true, 2) + 1);
                    }
                }
            }
        }
        return ans;
    }

    public int dfs(int curX, int curY, int direction, boolean canTurn, int target) {
        int nextX = curX + DIRS[direction][0];
        int nextY = curY + DIRS[direction][1];

        if (nextX < 0 || nextX >= m || nextY < 0 || nextY >= n || grid[nextX][nextY] != target) {
            return 0;
        }

        int turnInt = canTurn ? 1 : 0;
        if (memo[nextX][nextY][direction][turnInt] != -1) {
            return memo[nextX][nextY][direction][turnInt];
        }

        int steps = dfs(nextX, nextY, direction, canTurn, 2 - target);
        if (canTurn) {
            steps = Math.max(steps, dfs(nextX, nextY, (direction + 1) % 4, false, 2 - target));
        }
        memo[nextX][nextY][direction][turnInt] = steps + 1;
        return steps + 1;
    }
}