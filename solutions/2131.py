#https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/?envType=daily-question&envId=2025-05-25
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0

        reg = defaultdict(int)
        doub = defaultdict(int)

        for word in words:
            if word[0] == word[1]:
                doub[word] += 1
            else:
                reg[word] += 1
                if reg[word[1] + word[0]] >= reg[word]:
                    ans += 2

        odd_used = False
        for word in doub:
            if not odd_used and doub[word] % 2 == 1:
                odd_used = True
                ans += doub[word]
            else:
                ans += (doub[word] // 2) * 2
        return ans * 2