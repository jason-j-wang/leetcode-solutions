#https://leetcode.com/problems/palindrome-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        stack = []
        while fast != None:
            #odd length
            if fast.next == None:
                slow = slow.next
                break
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        while stack:
            x = stack.pop()
            if x != slow.val:
                return False
            slow = slow.next
        return True
        
        