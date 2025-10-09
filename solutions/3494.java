//https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/description/?envType=daily-question&envId=2025-10-09
class Solution {
    public long minTime(int[] skill, int[] mana) {
        int n = skill.length;

        long[] cur = new long[n];

        long offset = 0;

        for (int m : mana){
            long cur_time = cur[0];
            for (int i = 0; i < n; i++) {
                long processingTime = skill[i] * m;
                cur_time += processingTime;
                cur[i] = cur_time;

                if (i != n - 1 && cur_time + offset < cur[i+1]) {
                    offset += cur[i+1] - cur_time - offset;
                }    

            }

            for (int i = 0; i< n; i++) {
                cur[i] += offset;
            }
            offset = 0;

        }

        return cur[n - 1];
    }
}