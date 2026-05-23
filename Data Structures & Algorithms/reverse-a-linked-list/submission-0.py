# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr: # repeats until we get to the end of LL
            next_node = curr.next
            curr.next = prev # to reverse, we set the currents node next value to prev
            prev = curr # bring previous up
            curr = next_node # make curr the next node
        
        return prev
