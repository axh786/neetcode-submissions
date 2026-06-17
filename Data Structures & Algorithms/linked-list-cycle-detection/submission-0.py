# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        l = head
        r = head.next

        while l and r:
            if l == r:
                return True
            
            l = l.next
            r = r.next
            
            if r:
                r = r.next
            
            else:
                return False
        
        return False



# slow = head Cleaner solution
# fast = head

# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next

#     if slow == fast:
#         return True

# return False