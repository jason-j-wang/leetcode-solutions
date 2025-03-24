#https://leetcode.com/problems/count-days-without-meetings/description/?envType=daily-question&envId=2025-03-24
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        last_meeting = 0
        ans = 0

        for start, end in meetings:
            if start > last_meeting + 1:
                ans += start - last_meeting - 1
            last_meeting = max(end, last_meeting)
            
        return ans + days - last_meeting


