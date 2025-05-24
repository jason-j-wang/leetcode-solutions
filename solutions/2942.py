#https://leetcode.com/problems/find-words-containing-character/description/?envType=daily-question&envId=2025-05-24
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            for c in words[i]:
                if c == x:
                    ans.append(i)
                    break
        return ans