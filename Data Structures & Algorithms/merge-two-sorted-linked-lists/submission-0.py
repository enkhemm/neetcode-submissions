# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        curr1 = list1
        curr2 = list2
        print(curr1.val, curr2.val)

        while curr1:
            if curr1.val <= curr2.val:
                res.val = curr1.val
                res.next = ListNode(-1)
                curr1 = curr1.next
            else:
                res.val = curr2.val
                res.next = ListNode(-1)
                curr2 = curr2.next

        while curr2:
            res.val = curr2.val
            res.next = ListNode(-1)
            curr2 = curr2.next


        return res

        



        