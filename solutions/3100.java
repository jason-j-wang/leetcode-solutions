//https://leetcode.com/problems/water-bottles-ii/description/?envType=daily-question&envId=2025-10-02
class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int totalBottles = 0;

        while (numBottles >= numExchange) {
            totalBottles += numExchange;
            numBottles -= numExchange - 1;
            numExchange++;
        }

        return totalBottles + numBottles;
    }
}