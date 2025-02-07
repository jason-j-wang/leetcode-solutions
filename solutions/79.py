#https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, word, 0, board, visited):
                        return True
        return False


    def dfs(self, row, col, word, cur_idx, board, visited):
        if visited[row][col]:
            return False

        if cur_idx == len(word)-1 and board[row][col] == word[cur_idx]:
            return True

        if board[row][col] != word[cur_idx]:
            return False

        n = len(visited)
        m = len(visited[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        visited[row][col] = True
        for vert, hor in directions:
            new_row = row + vert
            new_col = col + hor
            if new_row >= 0 and new_row < n and new_col >= 0 and new_col < m:
                if self.dfs(new_row, new_col, word, cur_idx + 1, board, visited):
                    return True
        visited[row][col] = False
        return False