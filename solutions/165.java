//https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2025-09-23
class Solution {
    public int compareVersion(String version1, String version2) {
        String[] v1Split = version1.split("\\.");
        String[] v2Split = version2.split("\\.");

        int len = Math.max(v1Split.length, v2Split.length);

        for (int i = 0; i < len; i++) {
            int v1, v2;

            if (i >= v1Split.length) {
                v1 = 0;
            } else {
                v1 = Integer.parseInt(v1Split[i]);
            }

            if (i >= v2Split.length) {
                v2 = 0;
            } else {
                v2 = Integer.parseInt(v2Split[i]);
            }

            if (v1 < v2) {
                return -1;
            } else if (v1 > v2) {
                return 1;
            }
        }

        return 0;
    }
}