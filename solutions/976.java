//https://leetcode.com/problems/largest-perimeter-triangle/description/?envType=daily-question&envId=2025-09-28
class Solution {
    public int largestPerimeter(int[] nums) {
        Arrays.sort(nums);

        for (int i = nums.length - 1; i > 1; i--) {
            if (nums[i-1] + nums[i-2] > nums[i]) {
                return nums[i-1] + nums[i-2] + nums[i];
            }
        }

        return 0;
    }
}