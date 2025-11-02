#https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/?envType=daily-question&envId=2025-11-02
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        sentinel = ListNode(-1)
        prev = sentinel

        while head is not None:
            if head.val not in nums:
                prev.next = head
                prev = prev.next
            head = head.next
            prev.next = None

        return sentinel.next
            