//https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/?envType=daily-question&envId=2025-02-03
class Solution {
    public int minGroups(int[][] intervals) {
        ArrayList<int[]> events = new ArrayList<>();

        for (int[] interval : intervals) {
            events.add(new int[] {interval[0], 1});
            events.add(new int[] {interval[1] + 1, -1});
        }

        Collections.sort(events, (i1, i2) -> {
            if (i1[0] == i2[0]) {
                return i1[1] - i2[1];
            } else {
                return i1[0] - i2[0];
            }
        });

        int cur = 0;
        int ans = 0;

        for (int[] e : events) {
            cur += e[1];
            ans = Math.max(cur, ans);
        }
        return ans;
    }   
}