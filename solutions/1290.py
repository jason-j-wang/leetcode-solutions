#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/1696931541/?envType=daily-question&envId=2025-07-14
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0

        while head:
            ans = (ans << 1) | head.val
            head = head.next
        return ans