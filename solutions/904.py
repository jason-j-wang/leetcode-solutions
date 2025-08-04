#https://leetcode.com/problems/fruit-into-baskets/description/?envType=daily-question&envId=2025-08-04
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        n = len(fruits)
        cur_fruits = 0
        count = defaultdict(int)
        cur_types = set()
        ans = 0

        for right in range(n):
            f = fruits[right]

            cur_types.add(f)
            cur_fruits += 1
            count[f] += 1

            while len(cur_types) > 2:
                l = fruits[left]
                count[l] -= 1
                cur_fruits -= 1

                if count[l] == 0:
                    cur_types.remove(l)

                left += 1

            ans = max(ans, cur_fruits)
        return ans