//https://leetcode.com/problems/best-sightseeing-pair/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int left= 0;
        int right = 2;
        int cur_max = values[0] + values[1] - 1;

        while (right < values.length) {
            if (values[right-1]+values[right] - 1 > values[left] + values[right] + left - right) {
                left = right-1;
            } 
            cur_max = Math.max(cur_max, values[left] + values[right] + left - right);
            right++;
        }
        return cur_max;
    }
}