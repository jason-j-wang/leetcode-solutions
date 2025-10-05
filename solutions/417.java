//https://leetcode.com/problems/pacific-atlantic-water-flow/description/?envType=daily-question&envId=2025-10-05
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        boolean[][] pacific = bfs(heights, true);
        boolean[][] atlantic = bfs(heights, false);
        List<List<Integer>> ans = new ArrayList<>();
        int n = heights.length, m = heights[0].length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m ; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    List<Integer> cell = new ArrayList<>(List.of(i, j));
                    ans.add(cell);
                }
            }
        }

        return ans;
    }

    public boolean[][] bfs(int[][] heights, boolean pacific) {
        int n = heights.length, m = heights[0].length;
        int[] dRow = {0, 0, 1, -1};
        int[] dCol = {1, -1, 0, 0};

        boolean[][] visited = new boolean[n][m];

        Queue<Integer[]> q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            if (pacific) {
                q.add(new Integer[]{i, 0});
                visited[i][0] = true;
            } else {
                q.add(new Integer[]{i, m - 1});
                visited[i][m-1] = true;
            }
            
        }

        for (int j = 0; j < m; j++) {
            if (pacific) {
                q.add(new Integer[]{0, j});
                visited[0][j] = true;
            } else {
                q.add(new Integer[]{n - 1, j});
                visited[n-1][j] = true;
            }
            
        }

        while (!q.isEmpty()) {
            Integer[] cell = q.poll();
            int i = cell[0], j = cell[1];

            for (int dir = 0; dir < 4; dir++) {
                int ni = i + dRow[dir];
                int nj = j + dCol[dir];

                if (ni >= 0 && ni < n && nj >= 0 && nj < m && !visited[ni][nj] && heights[ni][nj] >= heights[i][j]) {
                    q.add(new Integer[]{ni, nj});
                    visited[ni][nj] = true;
                }
            }
        }

        return visited;
    }
}