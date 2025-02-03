#https://leetcode.com/problems/string-compression-iii/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""

        count = 1
        char = word[0]
        for i in range(1, len(word)):
            if word[i] != char:
                ans += str(count)
                ans += char

                char = word[i]
                count = 1
            elif count == 9:
                ans += str(count)
                ans += char

                count = 1
            else:
                count += 1

        ans += str(count)
        ans += char

        return ans

        