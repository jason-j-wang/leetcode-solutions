#https://leetcode.com/problems/interval-list-intersections/description/
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr_1 = 0
        ptr_2 = 0

        list_1_length = len(firstList)
        list_2_length = len(secondList)

        ans = []

        while ptr_1 < list_1_length and ptr_2 < list_2_length:
            start_1, end_1 = firstList[ptr_1]
            start_2, end_2 = secondList[ptr_2]

            #check if overlap
            if start_1 <= end_2 and start_2 <= end_1:
                ans.append([max(start_1, start_2), min(end_1, end_2)])

            if end_1 < end_2:
                ptr_1 += 1
            elif end_1 > end_2:
                ptr_2 += 1
            else:
                ptr_1 += 1
                ptr_2 += 1

        return ans