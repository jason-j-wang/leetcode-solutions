#https://leetcode.com/problems/finding-3-digit-even-numbers/description/?envType=daily-question&envId=2025-05-12
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        arr = []
        c = Counter(digits)
        for i in range(100, 1000, 2):
            cur_c = defaultdict(int)
            for d in str(i):
                cur_c[int(d)] += 1
            valid = True
            for d in cur_c:
                if c[d] < cur_c[d]:
                    valid = False

            if valid:
                arr.append(i)
        return arr