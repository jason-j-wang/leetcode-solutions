//https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/?envType=daily-question&envId=2025-10-10
class Solution {
    public int maximumEnergy(int[] energy, int k) {
        int ans = Integer.MIN_VALUE;

        int[] suffix = new int[k];

        for (int start = energy.length - 1; start >= 0; start--) {
            int idx = start % k;
            suffix[idx] += energy[start];
            ans = Math.max(ans, suffix[idx]);
        }

        return ans;
    }
}