#https://leetcode.com/problems/circular-sentence/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split(" ")
        for i in range(len(s) - 1):
            if s[i][-1] != s[i+1][0]:
                return False
        
        return s[-1][-1] == s[0][0]