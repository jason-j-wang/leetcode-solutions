#https://leetcode.com/problems/meeting-rooms-iii/submissions/1693791797/?envType=daily-question&envId=2025-07-11
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms, used_rooms = [i for i in range(n)], []
        meeting_count = [0] * n
        meetings.sort()
        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)
            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, (end, room))
            else:
                room_end_time, room = heappop(used_rooms)
                heappush(used_rooms, (room_end_time + end - start, room))
            meeting_count[room] += 1
        
        best = max(meeting_count)
        for i in range(n):
            if meeting_count[i] == best:
                return i
                

