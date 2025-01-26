//https://leetcode.com/problems/map-of-highest-peak/?envType=daily-question&envId=2025-01-26
class Solution {
    public int[][] highestPeak(int[][] isWater) {
        int n = isWater.length;
        int m = isWater[0].length;

        boolean[][] visited = new boolean[n][m];
        int[][] height = new int[n][m];
        Queue<int[]> q = new LinkedList<>();

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int i = 0; i < n; i++) {
            for  (int j = 0; j < m; j++) {
                if (isWater[i][j] == 1) {
                    q.offer(new int[]{i, j});
                    visited[i][j] = true;
                }
            }
        }

        while (!q.isEmpty()) {
            int[] node = q.peek();
            q.poll();

            int i = node[0];
            int j = node[1];
            int h = height[i][j];

            for (int[] d : directions) {
                int new_i = i + d[0];
                int new_j = j + d[1];

                if (valid(new_i, new_j, n, m) && !visited[new_i][new_j]) {
                    height[new_i][new_j] = h + 1;
                    visited[new_i][new_j] = true;
                    q.offer(new int[]{new_i, new_j});
                }
            }
        }
        return height;
    }


    public boolean valid(int i, int j, int n, int m) {
        return i >= 0 && i < n && j >= 0 && j < m;
    }
}
