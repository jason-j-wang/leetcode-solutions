#https://leetcode.com/problems/assign-elements-to-groups-with-constraints/description/?slug=count-substrings-divisible-by-last-digit&region=global_v2
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:

        d = {}
        max_num = max(groups)
        for i in range(len(elements)):
            num = elements[i]
            if num not in d:
                while num <= max_num:
                    if num not in d:
                        d[num] = i
                    num += elements[i]
        ans = []

        for i in range(len(groups)):
            num = groups[i]
            if num in d:
                ans.append(d[num])
            else:
                ans.append(-1)

        return ans

        