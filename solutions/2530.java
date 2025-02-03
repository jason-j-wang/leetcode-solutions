//https://leetcode.com/problems/maximal-score-after-applying-k-operations/?envType=daily-question&envId=2025-02-03
class Solution {
    public long maxKelements(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int n : nums) {
            pq.offer(n);
        }
        long score = 0;
        for (int i = 0; i < k; i++) {
            int num = pq.poll();
            score += num;

            num = (num % 3 == 0) ? num / 3 : num / 3 + 1;

            pq.offer(num);
        }

        return score;
    }
}