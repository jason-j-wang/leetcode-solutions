#https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/?envType=daily-question&envId=2025-05-03
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        ans = n + 1

        nums = [tops[0], bottoms[0]]


        for num in nums:
            top = 0
            bot = 0
            valid = True

            for i in range(n):
                if tops[i] != num:
                    if bottoms[i] == num:
                        top += 1
                    else:
                        valid = False
                        break

                if bottoms[i] != num:
                    if tops[i] == num:
                        bot += 1
                    else:
                        valid = False
                        break


            if valid:
                ans = min(ans, top, bot)
        
        return ans if ans != n + 1 else -1
