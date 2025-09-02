//https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/description/?envType=daily-question&envId=2025-09-02
class Solution {
    public int numberOfPairs(int[][] points) {
        Arrays.sort(points, (a, b) -> {
            if (a[0] != b [0]) {
                return Integer.compare(a[0], b[0]);
            } else {
                return Integer.compare(b[1], a[1]);
            }
            
        });
        int ans = 0;

        for (int i = 0; i < points.length; i++) {
            int[] p = points[i];
            int bottomThreshold = p[1];
            int topThreshold = Integer.MAX_VALUE;
            boolean sameX = false;

            for (int j = i - 1; j >= 0; j--) {
                if (bottomThreshold == topThreshold) {
                    break;
                }

                int[] q = points[j];

                if (q[1] < topThreshold && q[1] >= bottomThreshold) {
                    ans++;
                    topThreshold = Math.min(topThreshold, q[1]);
                }
            }
        }

        return ans;
    }
}