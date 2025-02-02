#https://leetcode.com/problems/count-mentions-per-user/description/
class Solution:
    def compare(self, a, b):
        if int(a[1]) != int(b[1]):
            return int(a[1]) - int(b[1])

        return -1 if a[0] == "OFFLINE" else 1

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=cmp_to_key(self.compare))

        online = [0 for i in range(numberOfUsers)]
        mentions = [0 for i in range(numberOfUsers)]
        all_increment = 0
        cur_time = 0

        for event in events:
            command = event[0]
            cur_time = int(event[1])
            user = event[2]

            if command == "MESSAGE":
                if user == "ALL":
                    all_increment += 1
                elif user == "HERE":
                    for i in range(numberOfUsers):
                        if online[i] <= cur_time:
                            mentions[i] += 1
                else:
                    people = user.split(" ")
                    for person in people:
                        id = int(person.split("id")[1])
                        mentions[id] += 1
            else:
                cur_time = int(event[1])
                user = int(event[2])
                online[user] = cur_time + 60
        if all_increment:
            for i in range(numberOfUsers):
                mentions[i] += all_increment
        return mentions