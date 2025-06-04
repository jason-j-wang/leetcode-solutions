#https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/?envType=daily-question&envId=2025-06-04
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        letter = word[0]
        pos = []

        for i, c in enumerate(word):
            if c > letter:
                letter = c
                pos = [(c, i)]
            elif c == letter:
                pos.append((c, i))

        ans = ""

        for c, i in pos:
            splits_left = numFriends - i

            cur_word = word[i:len(word) -splits_left + 1]

            if cur_word > ans:
                ans = cur_word
        return ans