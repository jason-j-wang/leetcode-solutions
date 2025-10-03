//https://leetcode.com/problems/trapping-rain-water-ii/description/?envType=daily-question&envId=2025-10-03
class Solution {
    public int trapRainWater(int[][] heightMap) {
        int[] dRow = { 0, 0, -1, 1 };
        int[] dCol = { -1, 1, 0, 0 };

        int n = heightMap.length;
        int m = heightMap[0].length;

        boolean[][] visited = new boolean[n][m];

        PriorityQueue<Integer[]> pq = new PriorityQueue<>((a, b) -> a[0].compareTo(b[0]));

        for (int i = 0; i < n; i++) {
            pq.add(new Integer[]{heightMap[i][0], i, 0});
            pq.add(new Integer[]{heightMap[i][m - 1], i, m - 1});

            visited[i][0] = true;
            visited[i][m-1] = true;
        }

        for (int j = 1; j < m - 1; j++) {
            pq.add(new Integer[]{heightMap[0][j], 0, j});
            pq.add(new Integer[]{heightMap[n - 1][j], n - 1, j});

            visited[0][j] = true;
            visited[n - 1][j] = true;
        }

        int ans = 0;

        while (!pq.isEmpty()) {
            Integer[] cell = pq.poll();
            int h = cell[0], i = cell[1], j = cell[2];

            for (int dir = 0; dir < 4; dir++) {
                int ni = i + dRow[dir];
                int nj = j + dCol[dir];

                if (ni >= 0 && ni < n && nj >= 0 && nj < m && !visited[ni][nj]) {
                    int nh = heightMap[ni][nj];

                    if (nh < h) {
                        ans += h - nh;
                    }

                    pq.add(new Integer[]{Math.max(nh, h), ni, nj});
                    visited[ni][nj] = true;
                }
            }
        }
        return ans;
    }
}