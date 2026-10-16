# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # secind attampt solution

        # ptr1, ptr2 = list1, list2
        # res = ListNode()
        # head = res.next

        # ptr_res = res

        # 0, 1,  ptr1
        # 2, 3   ptr2
        
        # temp = 1
        # res -> 0


        # temp = ptr1.next
        # res.next = ptr1
        # # ptr1.next = ptr2
        # ptr1 = temp
        ptr1, ptr2 = list1, list2
        res = ListNode()
        head = res

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                # temp = ptr1
                res.next = ptr1
                res = res.next
                ptr1 = ptr1.next
            else:
                res.next = ptr2
                res = ptr2
                ptr2 = ptr2.next

        while ptr1:
            res.next = ptr1
            res = ptr1
            ptr1 = ptr1.next

        while ptr2:
            res.next = ptr2
            res = ptr2
            ptr2 = ptr2.next

        return head.next

        
        