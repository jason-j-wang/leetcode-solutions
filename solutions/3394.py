#https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/?envType=daily-question&envId=2025-03-25
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        hor = rectangles.copy()
        vert = rectangles

        hor.sort(key=lambda x: x[1])
        vert.sort()

        top = hor[0][3]
        hor_count = 0

        for i in range(1, len(hor)):
            if hor_count >= 2:
                return True
            startx, starty, endx, endy = hor[i]
            if starty >= top:
                hor_count += 1
 
            top = max(top, endy)


        top = vert[0][2]
        vert_count = 0
        for i in range(1, len(vert)):
            if vert_count >= 2:
                return True
            startx, starty, endx, endy = vert[i]
            if startx >= top:
                vert_count += 1
            
            top = max(top, endx)
        print(hor_count, vert_count)
        return hor_count >= 2 or vert_count >= 2