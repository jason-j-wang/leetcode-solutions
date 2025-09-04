#https://leetcode.com/problems/smallest-palindromic-rearrangement-i/
class Solution:
    def smallestPalindrome(self, s: str) -> str:

        n = len(s)
        mid = ""
        if n % 2 == 1:
            mid = s[(n - 1) // 2]
        
        freq = Counter(s)

        left = ""
        for char in sorted(freq):
            left += char * (freq[char] // 2)

        return left + mid + left[::-1]