//https://leetcode.com/problems/avoid-flood-in-the-city/description/?envType=daily-question&envId=2025-10-07
class Solution {
    public int[] avoidFlood(int[] rains) {
        int[] ans = new int[rains.length];

        Map<Integer, Integer> next = new HashMap<>();
        Map<Integer, Boolean> lakes = new HashMap<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int[] nextRain = new int[rains.length];

        for (int i = rains.length - 1; i >= 0; i--) {
            int lake = rains[i];

            if (next.containsKey(lake)) {
                nextRain[i] = next.get(lake);
            } else {
                nextRain[i] = -1;
            }
            next.put(lake, i);
        }

        for (int i = 0; i < rains.length; i++) {
            if (rains[i] == 0) {
                if (pq.isEmpty()) {
                    ans[i] = 1;
                } else {
                    int idx = pq.poll();
                    int lake = rains[idx];

                    lakes.put(lake, false);
                    ans[i] = lake;
                }
            } else {
                ans[i] = -1;
                int lake = rains[i];
                if (lakes.containsKey(lake) && lakes.get(lake)) {
                    return new int[]{};
                } 
                lakes.put(lake, true);
                if (nextRain[i] != -1) {
                    pq.add(nextRain[i]);
                }
                
            }
        }

        return ans;
    }
}