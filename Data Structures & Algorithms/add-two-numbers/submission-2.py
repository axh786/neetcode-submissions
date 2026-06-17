# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        pointer = output
        bit = 0
        l1_val = 0
        l2_val = 0

        while l1 or l2: # run when either list can go, we dont need both at the same time
            if l1: # whatever list is missing an item replace it with a 0
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            
            digit = l1_val + l2_val + bit
            
            bit = digit // 10 # 6 // 10 = 0 16 // 10 = 1
            digit %= 10 # 6 % 10 = 6 16 % 10 = 6

            pointer.next = ListNode(digit)
            pointer = pointer.next
            
        if bit:
            pointer.next = ListNode(bit)

        return output.next
