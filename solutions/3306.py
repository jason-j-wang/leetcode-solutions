#https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        consts = 0
        left = 0
        right = 0
        ans = 0
        vowels = ["a", "e", "i", "o", "u"]
        counts = {}
        for v in vowels:
            counts[v] = 0
        
        next_const = [0 for i in range(len(word))]
        last_const = len(word)

        for i in range(len(word) -1, -1, -1):
            next_const[i] = last_const
            if word[i] not in vowels:
                last_const = i

        
        while left <= right and right < len(word):

            if word[right] in counts:
                counts[word[right]] += 1
            else:
                consts += 1

            while consts > k:
                if word[left] in vowels:
                    counts[word[left]] -= 1
                else:
                    consts -= 1
                left += 1

            while right < len(word) and self.has_all(counts) and consts == k:
                ans += next_const[right] - right
                if word[left] in vowels:
                    counts[word[left]] -= 1
                else:
                    consts -= 1
                left += 1
            right += 1
        return ans
            
    def has_all(self, counts):
        for c in counts:
            if counts[c] == 0:
                return False
        return True