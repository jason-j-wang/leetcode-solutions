//https://leetcode.com/problems/replace-non-coprime-numbers-in-array/description/?envType=daily-question&envId=2025-09-16
class Solution {
    public List<Integer> replaceNonCoprimes(int[] nums) {
        List<Integer> ans = new LinkedList<>();

        for (int num : nums) {
            while (true) {
                int last = ans.isEmpty() ? 1 : ans.getLast();
                int gcd = getGcd(last, num);
                if (gcd == 1) {
                    break;
                }

                num *= ans.removeLast() / gcd;
            }
            ans.add(num);
        }
        return ans;
    }

    private int getGcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }

        return a;
    }
}