# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        # part 1 | splitting and merge the two halves
        def split_merge(linkedlist):
            if not linkedlist.next:
                return linkedlist
            start = linkedlist
            slow = linkedlist
            fast = linkedlist
            prev = linkedlist

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None # cut off the link

            return mergeSortedList(split_merge(start), split_merge(slow))



        # part 2 | merge two sorted lists
        def mergeSortedList(left,right):
            dummy = ListNode(0)
            temp = dummy
            first = left
            second = right

            while first and second:
                if first.val < second.val:
                    temp.next = first
                    temp = first
                    first = first.next
                else:
                    temp.next = second
                    temp = second 
                    second = second.next
            
            if first:
                temp.next = first
            if second:
                temp.next = second
            return dummy.next


        if head:
            return split_merge(head)