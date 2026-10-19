# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        # def __lt__(self, l2):
        #     return self.val < l2.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0 :
            return None

            """
            main func.. 
            lets
            helper function that merges 2 lists
            ok lets actually use a minheap
            first populate the heap with all the heads of the lists in the input
            go thru the entire heap and append to res dummy lis its a next up until  and then add it's next elemetn into the heap
            """
        dummy = ListNode(0)
        curr = dummy
        heap = []

        for i,l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        while heap:
            smallest_val, ind, smallest_node = heapq.heappop(heap)
            curr.next = ListNode(smallest_val)
            curr = curr.next
            if smallest_node.next:
                heapq.heappush(heap, (smallest_node.next.val, ind, smallest_node.next))

        return dummy.next
        