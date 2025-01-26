//https://leetcode.com/problems/minimum-cost-for-tickets/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        Set<Integer> v = new HashSet<>();
        for (int d : days) {
            v.add(d);
        }
        int[] dp = new int[days[days.length-1]+1];
        Arrays.fill(dp, -1);

        return ans(costs, v, 1, dp);
        
    }

    public int ans(int[] costs, Set<Integer> days, int curDay, int[] dp) {

        if (curDay >= dp.length) {
            return 0;
        }

        if (dp[curDay] != -1) {
            return dp[curDay];
        }

        if (!days.contains(curDay)) {
            return ans(costs, days, curDay + 1, dp);
        }

        int one = costs[0] + ans(costs, days, curDay + 1, dp);
        int seven = costs[1]+ ans(costs, days, curDay + 7, dp);
        int thirty = costs[2] + ans(costs, days, curDay + 30, dp);

        int c = Math.min(one, Math.min(seven, thirty));

        dp[curDay] = c;
        return c;
    }
}
