#https://leetcode.com/problems/separate-squares-i/description/?envType=daily-question&envId=2026-01-13
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        lines = []

        for _, y, l in squares:
            total_area += l * l
            lines.append((y, l, 1))
            lines.append((y + l, l, -1))

        lines.sort(key=lambda x: x[0])

        curr_width = 0.0
        curr_area = 0.0
        prev_height = 0.0

        for y, l, delta in lines:
            diff = y - prev_height
            area = curr_width * diff

            if 2 * (curr_area + area) >= total_area:
                return prev_height + (total_area - 2 * curr_area) / (2 * curr_width)
            
            curr_width += delta * l
            curr_area += area
            prev_height = y

        return 0.0