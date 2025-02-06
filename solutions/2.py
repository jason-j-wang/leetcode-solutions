#https://leetcode.com/problems/add-two-numbers/description/?envType=problem-list-v2&envId=recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        cur = sentinel
        carry = 0

        while l1 != None or l2 != None:
            cur_sum = 0
            if l1:
                cur_sum += l1.val
                l1 = l1.next
            
            if l2:
                cur_sum += l2.val
                l2 = l2.next
            cur_sum += carry

            carry = cur_sum // 10
            node = ListNode(cur_sum % 10)
            cur.next = node
            cur = node

        if carry:
            cur.next = ListNode(carry)
        return sentinel.next