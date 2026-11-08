# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        sz = 0
        curr = head
        while curr:
            sz += 1
            curr = curr.next

        parent = None
        curr = head

        rem = sz - n
        if rem == 0:
            head = None
            return head


        while curr:
            if rem == 0:
                parent.next = curr.next
                break

            rem -= 1
            parent = curr
            curr = curr.next

        
        return head     