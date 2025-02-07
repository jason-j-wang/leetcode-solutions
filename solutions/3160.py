#https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/?envType=daily-question&envId=2025-02-07
class Solution:
    #edge cases:
    # no balls: return 0
    # no queries: return 0
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        number_present_colours = 0
        occurences_of_each_colour = defaultdict(int)
        ball_colours = defaultdict(int)
        ans = []

        for ball, colour in queries:
            cur_ball_colour = ball_colours[ball]

            if cur_ball_colour > 0:
                occurences_of_each_colour[cur_ball_colour] -= 1

                # decrementing colour counter if no more of this colour in array
                if occurences_of_each_colour[cur_ball_colour] == 0:
                    number_present_colours -= 1

            #assign ball the new colour
            occurences_of_each_colour[colour] += 1
            ball_colours[ball] = colour

            # check if this is the first instance of the colour in ball array
            if occurences_of_each_colour[colour] == 1:
                number_present_colours += 1

            ans.append(number_present_colours)
        return ans