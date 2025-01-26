#https://leetcode.com/problems/construct-string-with-repeat-limit/description/?envType=daily-question&envId=2025-01-26
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1


        letters = list(counts.keys())
        letters.sort(reverse=True)

        if len(letters) == 1:
            return letters[0] * repeatLimit

        cur_idx = 0
        next_idx = 1
        ans = ""
        while True:
            cur_letter = letters[cur_idx]
            for i in range(repeatLimit):
                if counts[cur_letter] >= 1:
                    ans += cur_letter
                    counts[cur_letter] -=1
                
                if counts[cur_letter] == 0:
                    break
           

            if counts[cur_letter] == 0:
                if next_idx == len(letters):
                    return ans
                cur_idx = next_idx
                next_idx += 1
                while next_idx < len(letters) and counts[letters[next_idx]] == 0:
                    next_idx += 1
            else:
                if next_idx == len(letters):
                    return ans
                ans += letters[next_idx]
                counts[letters[next_idx]] -=1

                if counts[letters[next_idx]] == 0:
                    while next_idx < len(letters) and counts[letters[next_idx]] == 0:
                        next_idx += 1
        return ans


            