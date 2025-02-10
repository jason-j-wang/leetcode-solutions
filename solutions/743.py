#https://leetcode.com/problems/network-delay-time/description/?envType=problem-list-v2&envId=shortest-path
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float("inf") for i in range(n+1)]
        distances[0] = 0
        adj_list = {}

        for source, target, time in times:
            if source not in adj_list:
                adj_list[source] = {}
            adj_list[source][target] = time

        queue = [(0, k)]
        longest_dist = 0
        while queue:
            cur_time, cur_node = heapq.heappop(queue)
            if distances[cur_node] == float("inf"):
                n -= 1
                longest_dist = cur_time
            else:
                continue

            if cur_time < distances[cur_node]:
                distances[cur_node] = cur_time

                if cur_node in adj_list:
                    for next_node in adj_list[cur_node]:
                        heapq.heappush(queue, (cur_time + adj_list[cur_node][next_node], next_node))

        return longest_dist if n == 0 else -1


        