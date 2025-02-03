//https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/?envType=daily-question&envId=2025-02-03

class Solution {
    public long dividePlayers(int[] skill) {
        int[] s = skill;
        Arrays.sort(s);

        int targetSkill = s[0] + s[s.length - 1];
        long totalChem = 0;

        for (int i = 0; i < s.length / 2; i++) {
            int p1 = s[i];
            int p2 = s[s.length - 1 - i];

            if (p1 + p2 != targetSkill) {
                return -1;
            }
            totalChem += p1 * p2;
        }

        return totalChem;
    }
}