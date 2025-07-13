#https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/?envType=daily-question&envId=2025-07-13
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        t = len(trainers)
        ans = 0
        t_ptr = 0

        for p in players:
            if t_ptr == t:
                return ans
            if p <= trainers[t_ptr]:
                ans += 1
                t_ptr += 1

        return ans