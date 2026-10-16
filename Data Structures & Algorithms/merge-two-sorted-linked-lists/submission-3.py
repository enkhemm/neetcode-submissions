# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # res = ListNode(-1)
        # curr1 = list1
        # curr2 = list2
        # print(list1.val)

        # while list1:
        #     if list1.val <= list2.val:
        #         res.val = list1.val
        #         res.next = ListNode(-1)
        #         res = res.next
        #         list1 = list1.next
        #     else:
        #         res.val = list2.val
        #         res.next = ListNode(-1)
        #         res = res.next
        #         list2 = list2.next

        # while list2:
        #     res.val = list2.val
        #     res.next = ListNode(-1)
        #     res = res.next
        #     list2 = list2.next


        # return res

        # res = ListNode()
        # node = res
 
        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         node.val = list1.val
        #         list1 = list1.next

        #     else:
        #         node.val = list2.val
        #         list2 = list2.next
            
        #     if not list1 or not list2:
        #         continue
        #     node.next = ListNode()
        #     node = node.next

        # node.next = list1 if list1 else list2

        # return res

        temp = ListNode()
        tail = temp

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return temp.next
        



        