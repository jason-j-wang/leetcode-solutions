#https://leetcode.com/problems/word-search-ii/description/
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words) -> None:
        
        for word in words:
            cur_node = self.root
            for c in word:
                if c not in cur_node.children:
                    cur_node.children[c] = TrieNode()
                cur_node = cur_node.children[c]        
            cur_node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefix_tree = Trie()
        prefix_tree.insert(words)

        root = prefix_tree.root
        ans = []
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in root.children:
                    self.traverse(board,root, ans, row, col)
        return ans

    def traverse(self, board, trie_node, ans, row, col):
        rows = len(board)
        cols = len(board[0])
        if board[row][col] == "#" or board[row][col] not in trie_node.children:
            return
        char = board[row][col]
        
        next_trie = trie_node.children[char]
        # if we reach trie with is_end = True
        if next_trie.word != None and next_trie.word not in ans:
            ans.append(next_trie.word)

        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        board[row][col] = "#"
        for vert, hor in directions:
            new_row = row + vert
            new_col = col + hor
            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                self.traverse(board, next_trie, ans, new_row, new_col)
        board[row][col] = char
        
        