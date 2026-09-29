# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        why even need to tracck index
        recursion?
        if i am a null return false
        if not i = next node
        index

        or use a set to record the addressses
        start from the beginning while head is not null
        if not in set
        record into set
        move on
        else return fasle

        """

        seen = set()
        while head:
            if head not in seen:
                seen.add(head)
                head = head.next
            else:
                return True

        
        return False
        