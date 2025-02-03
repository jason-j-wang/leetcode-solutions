//https://leetcode.com/problems/maximum-width-ramp/description/?envType=daily-question&envId=2025-02-03
class Solution {
    public int maxWidthRamp(int[] nums) {
        int n = nums.length;
        Stack<Integer> s = new Stack<>();
        s.push(0);
        int ans = -1;

        for (int i = 1; i < n; i++) {
            if (nums[i] <= nums[s.peek()]) {
                s.push(i);
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            while (!s.isEmpty() && nums[s.peek()] <= nums[i]) {
                ans = Math.max(ans, i - s.peek());
                s.pop();
            }
 
        }

        return ans;
    }
}
