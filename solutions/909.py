#https://leetcode.com/problems/snakes-and-ladders/description/?envType=daily-question&envId=2025-05-31
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        dist = [float('inf') for _ in range(n**2 + 1)]
        flattened = [-1 for _ in range(n**2 + 1)]
        rev = False
        for i in range(n-1, -1, -1):
            for j in range(n):
                num = (n - i - 1) * n + j + 1 if not rev else (n - i) * n - j
                flattened[num] = board[i][j]
            rev = not rev

        q = deque([(0, 1)])

        while q:
            num_rolls, square = q.popleft()

            if dist[square] > num_rolls:
                dist[square] = num_rolls

                for i in range(1, 7):
                    next_square = square + i
                    if next_square <= n ** 2:
                        
                        if flattened[next_square] != -1:
                            next_square = flattened[next_square]

                        if num_rolls + 1 < dist[next_square]:
                            q.append((num_rolls + 1, next_square))
        return dist[n**2] if dist[n**2] != float('inf') else -1
