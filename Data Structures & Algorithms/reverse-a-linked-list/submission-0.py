# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # if head.next == None:
        #     return []

        # curr = head
        # prev = ListNode()


        # # switch last
        # # keep going until end of 
        # while not curr:
        #     prev = curr
        #     curr = curr.next

        # curr.next = prev
        # curr = prev
        # more = ListNode()
        # while curr 


        # start from head:
        #     curr = end of list
        #     curr = head.next

        # # not curr and prev BUT curr and next
        # # how to get the prev node after finishin??
        # nextNode = head.next
        # curr = head
        # while not nextNode:
        #     curr = nextNode
        #     nextNode = nextNode.next
        # while

        #3 prev, curr = head and temp..

        #[0,1,2,3]
        prev, curr = None, head

        #[p=2,c=3, t=N]
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev









        