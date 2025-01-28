//https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/?envType=daily-question&envId=2025-01-28
class Solution {
    public int findMaxFish(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int ans = 0;
        boolean[][] visited = new boolean[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] > 0 && !visited[i][j]) {
                    ans = Math.max(ans, bfs(i, j, grid, visited));
                }
            }
        }
        return ans;

    }

    public int bfs(int r, int c, int[][] grid, boolean[][] visited) {
        int fish = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{r, c});

        while (!q.isEmpty()) {
            int[] coord = q.peek();
            int x = coord[0];
            int y = coord[1];
            q.poll();
            fish += grid[x][y];
            visited[x][y] = true;

            for (int[] d : directions) {
                if (x + d[0] >= 0 && x + d[0] < rows && y + d[1] >= 0 && y + d[1] < cols && !visited[x+d[0]][y+d[1]] && grid[x+d[0]][y+d[1]] > 0) {
                    q.offer(new int[]{x + d[0], y + d[1]});
                    visited[x+d[0]][y+d[1]] = true;
                }
            }

        }
        return fish;
    }   
}