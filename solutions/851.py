#https://leetcode.com/problems/loud-and-rich/description/?envType=problem-list-v2&envId=depth-first-search
class Solution:
    # edge cases:
    # if no one has more money than person a, x[a] = a
    #question is worded weirdly, actually want to find quietest person

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj_list = [[] for _ in range(n)]
        ans = [-1] * n

        # building adj list
        for rich, poor in richer:
            adj_list[poor].append(rich)

        # building the answer
        for i in range(len(ans)):
            self.find_loudest(adj_list, i, quiet, ans)

        return ans

    # returns the index of person who is the loudest
    def find_loudest(self, adj_list, cur_person, quiet, ans):

        if ans[cur_person] != -1:
            return ans[cur_person]

        loudest = quiet[cur_person]
        loudest_person = cur_person

        for richer in adj_list[cur_person]:
            potential_loudest = self.find_loudest(adj_list, richer, quiet, ans)
            if quiet[potential_loudest] < loudest:
                loudest = quiet[potential_loudest]
                loudest_person = potential_loudest
        
        ans[cur_person] = loudest_person
        return loudest_person