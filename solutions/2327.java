//https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/?envType=daily-question&envId=2025-09-09
class Solution {
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        int mod = (int) Math.pow(10, 9) + 7;
        int[] numPeopleLearned = new int[n];
        numPeopleLearned[0] = 1;
        int curPeopleTelling = 0;
        int totalKnow = 1;

        for (int day = 1; day < n; day++) {
            if (day - delay >= 0) {
                curPeopleTelling = (curPeopleTelling + numPeopleLearned[day - delay]) % mod;
            }

            if (day - forget >= 0) {
                curPeopleTelling = (curPeopleTelling - numPeopleLearned[day - forget]) % mod;
                totalKnow = (totalKnow - numPeopleLearned[day - forget]) % mod;

                if (curPeopleTelling < 0) {
                    curPeopleTelling += mod;
                }

                if (totalKnow < 0) {
                    totalKnow += mod;
                }
            }

            numPeopleLearned[day] = curPeopleTelling;
            totalKnow = (totalKnow + curPeopleTelling) % mod;
        }

        return totalKnow;

    }
}