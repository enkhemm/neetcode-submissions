# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """

        # """
        # [1] n = 0
        
        # if not head:
        #     return head

        # cnt = 0

        # prev = None
        # curr = head
        # while curr:
        #     if cnt == n:
        #         prev.next = curr.next
        #         curr.next = None
        #     else:
        #         prev = curr
        #         curr = curr.next
        #         cnt += 1

        # return head\\

        # [1,2,3,4]
        # cnt = 1
        # node = 1
        # prev = n

        # helper(1, n, 1)
        # helper(2, 1, 2)
        # helper(3, 2, 3)
        # helper(4, 3, 4)
        # helper(n, 4, 5)
        # to_del = 4 

        to_del_cnt = 0
        if n == 1:
            head = None
            return head
        def helper(node, prev, cnt):
            if node:
                # prev = node
                helper(node.next, node, cnt+1)
            if not node:
                nonlocal to_del_cnt
                to_del_cnt = cnt - n
            if cnt == to_del_cnt:
                prev.next = node.next
                node.next = None
            

        helper(head, None, 1)
        return head



        
               
