#https://leetcode.com/problems/find-special-substring-of-length-k/?slug=select-k-disjoint-special-substrings&region=global_v2
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:

        if len(s) == 1:
            return True
        cur_char = s[0]
        left = 0
        right = 0

        while left <= right and right < len(s):
            if right - left + 1 == k:
                if s[right] == s[left] and (right + 1 == len(s) or s[right+1] != s[left]):
                    return True
                else:
                    while right < len(s) and s[right] == s[left]:
                        right += 1
                    left = right
            elif s[right] == s[left]:
                right += 1
            else:
                right += 1
                left = right - 1

        return False