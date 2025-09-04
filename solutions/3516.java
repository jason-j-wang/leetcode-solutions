//https://leetcode.com/problems/find-closest-person/description/?envType=daily-question&envId=2025-09-04
class Solution {
    public int findClosest(int x, int y, int z) {
        return Math.abs(x - z) < Math.abs(y - z) ? 1 : (Math.abs(x - z) == Math.abs(y - z) ? 0 : 2);
    }
}