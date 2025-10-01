//https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2025-10-01
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int fullBottles = numBottles;
        int emptyBottles = 0;
        int totalBottles = 0;

        while (true) {
            // Drinking step
            totalBottles += fullBottles;
            emptyBottles += fullBottles;

            if (emptyBottles < numExchange) {
                break;
            }

            // Exchanging step
            fullBottles = emptyBottles / numExchange;
            emptyBottles = emptyBottles % numExchange;
        }


        return totalBottles;
    }
}