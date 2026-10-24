# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        head
        prev of tail
        tail
        temp = to store future ones
        [0-h, 6 - t, 1-t, 2, 3, 4, 5-p]

        h = t
        p = t

        [0, 2, 3, 4]; new_l = [6, 5, 4]
        [0, 1, 2, 3, 4, 5, 6]

        count

        divide the list into haves, where 1 bigger or ceil(7/2)!

        new head at divide head2 = // need to null out the last index of head??
        reverse the second half
        merge the two

        """
        if not head:
            return

        len_list = 0

        #count 
        curr = head
        # count = 0
        while curr:
            len_list += 1
            curr = curr.next

        divide_ind = math.ceil(len_list/2) # 4

        # separate lists
        curr = head
        for i in range(1, divide_ind):
            curr = curr.next    

        # 

        head2 = curr.next
        curr.next = None

        # prev-> None head -> 4, 5, 6, 7
        # reversed 2nd half
        prev = None
        curr = head2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head2 = prev


        #Merge
        # 1,  2, 3    7, 6, 
        # 1  2

        while head2:
            temp = head.next
            temp2 = head2.next
            head.next = head2 
            head2.next = temp

            # head = head.next # why this doesn/t work i have no idea???????
            # head2 = temp2
            head = temp
            head2 = temp2









        