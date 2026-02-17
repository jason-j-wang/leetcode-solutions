//https://leetcode.com/problems/binary-watch/description/?envType=daily-question&envId=2026-02-17
class Solution {
    public List<String> readBinaryWatch(int turnedOn) {
        List<String> ans = new ArrayList<>();

        if (turnedOn > 8) {
            return ans;
        }

        solve(turnedOn, 0, 0, 0, 0, ans);
        return ans;

    }

    private void solve(int numBits, int hourPtr, int minPtr, int curHour, int curMin, List<String> ans) {
        if (curHour > 11 || curMin > 59) {
            return;
        }

        if (numBits == 0) {
            addTime(curHour, curMin, ans);
            return;
        }

        if (hourPtr == 4 && minPtr == 6) {
            return;
        }

        int[] hours = {8, 4, 2, 1};
        int[] mins = {32, 16, 8, 4, 2, 1};
        
        if (hourPtr < 4) {
            solve(numBits - 1, hourPtr + 1, minPtr, curHour + hours[hourPtr], curMin, ans);
            solve(numBits, hourPtr + 1, minPtr, curHour, curMin, ans);
        } else {
            solve(numBits - 1, hourPtr, minPtr + 1, curHour, curMin + mins[minPtr], ans);
            solve(numBits, hourPtr, minPtr + 1, curHour, curMin, ans);
        }
    }

    private void addTime(int hour, int min, List<String> ans) {
 
        StringBuilder sb = new StringBuilder();
        sb.append(hour);
        sb.append(":");
        if (min < 10) {
            sb.append("0");
        }
        sb.append(min);
        ans.add(sb.toString());
    }
}