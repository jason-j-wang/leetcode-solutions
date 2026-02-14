//https://leetcode.com/problems/champagne-tower/description/?envType=daily-question&envId=2026-02-14
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] cups = new double[102][102];
        cups[0][0] = (double) poured;

        for (int row = 0; row <= query_row; row++) {
            for (int cup = 0; cup <= row; cup++) {
                double overflow = (cups[row][cup] - 1) / 2;
                if (overflow > 0) {
                    cups[row+1][cup] += overflow;
                    cups[row+1][cup+1] += overflow;
                }
            }
        }

        return Math.min(1, cups[query_row][query_glass]);
    }
}