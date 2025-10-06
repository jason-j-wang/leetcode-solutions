//https://leetcode.com/problems/swim-in-rising-water/description/?envType=daily-question&envId=2025-10-06
class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        int time = 0;
        boolean[][] visited = new boolean[n][m];

        PriorityQueue<Integer[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

        int[] dRow = {0, 0, 1, -1};
        int[] dCol = {1, -1, 0, 0};

        pq.add(new Integer[]{grid[0][0], 0, 0});
        visited[0][0] = true;

        while (!pq.isEmpty()) {
            Integer[] cell = pq.poll();
            int height = cell[0], i = cell[1], j = cell[2];

            time = Math.max(height, time);

            if (i == n - 1 && j == m - 1) {
                return time;
            }

            for (int dir = 0; dir < 4; dir++) {
                int ni = i + dRow[dir];
                int nj = j + dCol[dir];

                if (ni >= 0 && ni < n && nj >= 0 && nj < m && !visited[ni][nj]) {
                    pq.add(new Integer[]{grid[ni][nj], ni, nj});
                    visited[ni][nj] = true;
                }
            }

        }

        // Should never reach this
        return 0;
    }
}