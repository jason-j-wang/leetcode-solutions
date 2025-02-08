#https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=problem-list-v2&envId=trie
# first implementation
class TrieNode:
    def __init__(self, character, is_end):
        self.character = character
        self.is_end = is_end
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("", False)

    def insert(self, word: str) -> None:
        tnode, first_new_index = self.traverse_trie(self.root, word, 0)

        if first_new_index == len(word):
            tnode.is_end = True
            return
        
        tnode.children[word[first_new_index]] = self.build_trie(word[first_new_index:], 0)

    def search(self, word: str) -> bool:
        tnode, first_new_index = self.traverse_trie(self.root, word, 0)
        return first_new_index == len(word) and tnode.is_end
        
    def startsWith(self, prefix: str) -> bool:
        tnode, first_new_index = self.traverse_trie(self.root, prefix, 0)
        return first_new_index == len(prefix)
        
    def traverse_trie(self, tnode, current_string, current_index):
        if current_string[current_index] in tnode.children:
            child = current_string[current_index]
            if current_index == len(current_string) - 1:
                return tnode.children[child], current_index + 1
            return self.traverse_trie(tnode.children[child], current_string, current_index + 1)
        
        return tnode, current_index

    def build_trie(self, string, current_index):
        new_trie = TrieNode(string[current_index], False)
        if current_index == len(string)-1:
            new_trie.is_end = True
            return new_trie
        new_trie.children[string[current_index + 1]] = self.build_trie(string, current_index + 1)
        return new_trie

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


#second implementation
class TrieNode:
    def __init__(self, is_end):
        self.is_end = is_end
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode(False)

    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode(False)
            cur_node = cur_node.children[c]        
        cur_node.is_end = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node != None and node.is_end
        
    def startsWith(self, prefix: str) -> bool:
        node = self._traverse(prefix)
        return node != None

    def _traverse(self, string):
        cur_node = self.root
        for c in string:
            if c not in cur_node.children:
                return None
            cur_node = cur_node.children[c]
        return cur_node
        
   

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)