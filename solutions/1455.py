#https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        n = len(searchWord)

        for i in range(len(words)):
            if searchWord == words[i][:n]:
                return i + 1
        return -1