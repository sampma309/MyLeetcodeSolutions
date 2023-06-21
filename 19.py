# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        first = head
        second = head

        while first is not None:
            length += 1
            first = first.next

        if length == 1:
            return None

        elif n == length:
            return head.next
        else:
            for i in range(length - n - 1):
                second = second.next
            second.next = second.next.next
            return head
    
    
"""
On first pass, calculate length of linked list. Using a second pointer, iterate
through the list L-n-1 times to arrive at the node before the one to be removed.
Move that node's next pointer to next.next to cut out the desired node. 

Two special cases:
1. If the linked list contains only one node, return None because the only node
will be removed.
2. If the node to be removed is the head of the list, move the head pointer to
the node following the original head node.

Time complexity: O(N)
Space complexity: O(1)

Note: my original solution is below. Instead of using two pointers, it uses an
array to store a pointer to each node in the linked list. This solution has a
time and space complexity of O(N).
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        node_pointers = []

        cur = head
        while cur is not None:
            length += 1
            node_pointers.append(cur)
            cur = cur.next

        if length == 1:
            return None

        if n == length:
            head = head.next
        else:
            node_before_removal = node_pointers[length - n - 1]
            node_before_removal.next = node_before_removal.next.next

        return head
