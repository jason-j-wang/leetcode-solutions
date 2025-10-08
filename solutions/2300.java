//https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=daily-question&envId=2025-10-08
class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        Arrays.sort(potions);

        int[] ans = new int[spells.length];

        for (int i = 0; i < spells.length; i++) {
            long target = (success + spells[i] - 1) / spells[i];
            int idx = binarySearch(target, potions);
            ans[i] = potions.length - idx;
        }

        return ans;
    }

    public int binarySearch(long target, int[] potions) {
        int left = 0, right = potions.length;

        while (left < right) {
            int mid = (left + right) / 2;

            if (potions[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}