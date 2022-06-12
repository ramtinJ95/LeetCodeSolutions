# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous

# used less memory then 93 % of submissions
# this is O(n) time complexiy and O(1) memory complexity
# recursive solution gives the same time complexity but O(n) memory complexity since
# we need to keep a copy of the entire list essentially in memory. 