#https://leetcode.com/problems/rabbits-in-forest/description/?envType=daily-question&envId=2025-04-20
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = defaultdict(int)

        for a in answers:
            counts[a] += 1

        ans = 0

        for c in counts:
            if counts[c] <= c + 1:
                ans += c + 1
            else:
                ans += ((counts[c] + c) // (c+1)) * (c+1)

        return ans