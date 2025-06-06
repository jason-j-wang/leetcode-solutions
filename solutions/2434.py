#https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/?source=submission-ac
class Solution:
    def robotWithString(self, s: str) -> str:
        counts = defaultdict(int)
        n = len(s)

        for i in range(len(s)):
            counts[s[i]] += 1
        
        chars = list(counts.keys())
        chars.sort()

        len_c = len(chars)

        i = 0
        end = []
        start = ""

        j = 0
 

        for i in range(len(s)):
            if j < len_c:
                if s[i] == chars[j]:
                    start += s[i]
                    counts[chars[j]] -= 1

                    while j < len_c and counts[chars[j]] == 0:
                        j += 1

                        while end and end[-1] <= chars[j]:
                            start += end.pop()
                
                else:
                    end.append(s[i])
                    counts[s[i]] -= 1

        return start + "".join(end[::-1])



