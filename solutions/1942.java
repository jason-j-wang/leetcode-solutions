//https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/?envType=daily-question&envId=2025-02-03

class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        int n = times.length;
        int smallestChair = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int[] chairAssignment = new int[n];
        Integer[] arrivals = new Integer[n];
        Integer[] departures = new Integer[n];
        for (int i = 0; i < n; i++) {
            chairAssignment[i] = -1;
            arrivals[i] = i;
            departures[i] = i;
        }

        Arrays.sort(arrivals, (i, j) -> times[i][0] - times[j][0]);
        Arrays.sort(departures, (i, j) -> times[i][1] - times[j][1]);

        int arrivalPointer = 0;
        int departurePointer = 0;

        while (arrivalPointer < n) {
            if (times[arrivals[arrivalPointer]][0] < times[departures[departurePointer]][1]) {
                if (!pq.isEmpty()) {
                    chairAssignment[arrivals[arrivalPointer]] = pq.poll();
                } else {
                    chairAssignment[arrivals[arrivalPointer]] = smallestChair;
                    smallestChair++;
                }
                if (arrivals[arrivalPointer] == targetFriend) {
                    return chairAssignment[arrivals[arrivalPointer]];
                }
                arrivalPointer++;
            } else {
                int chair = chairAssignment[departures[departurePointer]];
                pq.add(chair);
                departurePointer++;
            }
        }
        return -1;

    }
}