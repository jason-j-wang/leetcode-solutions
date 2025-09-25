//https://leetcode.com/problems/triangle/description/?envType=daily-question&envId=2025-09-25
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        List<Integer> prev = triangle.get(0);

        for (int i = 1; i < triangle.size(); i++) {
            List<Integer> next = new ArrayList<>();
            List<Integer> cur = triangle.get(i);
            next.add(prev.get(0) +  cur.get(0));
            for (int j = 1; j < triangle.get(i).size() - 1; j++) {
                next.add(Math.min(prev.get(j) +  cur.get(j), prev.get(j-1) +  cur.get(j)));
            }
            next.add(prev.get(prev.size() - 1) + cur.get(cur.size() - 1));
            prev = next;
        }

        return Collections.min(prev);
    }
}