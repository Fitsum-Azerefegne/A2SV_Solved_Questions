class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            current = node

            while current:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            return prev

        head = reverse(head)
        maxVal = head.val
        current = head

        while current and current.next:
            if current.next.val < maxVal:
                current.next = current.next.next
            else:
                current = current.next
                maxVal = current.val  

        return reverse(head)