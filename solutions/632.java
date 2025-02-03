//https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/?envType=daily-question&envId=2025-02-03
class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int start = 0;
        int end = Integer.MAX_VALUE;
        int maxVal = Integer.MIN_VALUE;

        for (int i = 0; i < nums.size(); i++) {
            pq.offer(new int[] {nums.get(i).get(0), i, 0});
            maxVal = Math.max(maxVal, nums.get(i).get(0));
        }

        while (pq.size() == nums.size()) {
            int[] next = pq.poll();
            int val = next[0];
            int listNum = next[1];
            int idx = next[2];

            if (maxVal - val < end - start) {
                start = val;
                end = maxVal;
            }

            if (idx + 1 < nums.get(listNum).size()) {
                int newVal = nums.get(listNum).get(idx + 1);
                pq.offer(new int[] {newVal, listNum, idx+1});
                maxVal = Math.max(maxVal, newVal);
            }

        }
        return new int[] {start, end};

        
    }
}
