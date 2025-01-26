//https://leetcode.com/problems/bitwise-xor-of-all-pairings/?envType=daily-question&envId=2025-01-26
class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
  
        int ans = 0;
        if (nums1.length % 2 == 0 && nums2.length % 2 == 0) {
            return 0;
        }

        if (nums1.length % 2 == 1 && nums2.length % 2 == 0) {
            for (int num : nums2) {
                ans ^= num;
            }
            return ans;
        }

        if (nums1.length % 2 == 0 && nums2.length % 2 == 1) {
            for (int num : nums1) {
                ans ^= num;
            }
            return ans;
        }

        for (int num : nums1) {
            ans ^= num;
        }
        for (int num : nums2) {
            ans ^= num;
        }
        return ans;
    }
}