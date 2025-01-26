//https://leetcode.com/problems/target-sum/description/?envType=daily-question&envId=2025-01-26
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        Map<Pair<Integer, Integer>, Integer> dp = new HashMap<>();

        return ans(nums, target, 0, 0, dp);
    }

    public int ans(int[] nums, int target, int index, int curSum, Map<Pair<Integer, Integer>, Integer> dp) {
        Pair<Integer, Integer> np = new Pair<>(index, curSum);

        if (dp.containsKey(np)) {
            return dp.get(np);
        }

        if (index == nums.length && curSum == target) {
            return 1;
        }

        if (index == nums.length) {
            return 0;
        }

        dp.put(np, ans(nums, target, index + 1, curSum + nums[index], dp) + ans(nums, target, index + 1, curSum - nums[index], dp));

        return dp.get(np);
    }
}
