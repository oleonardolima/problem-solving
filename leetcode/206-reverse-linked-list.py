# Problem Statement: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # To reverse the linked list we need to iterate through the linked list keeping the previoud node
        
        # Iteratively we have:
        if head != None:
            prev_node = None
            next_node = head.next
            while (next_node != None):
                head.next = prev_node
                prev_node = head
                head = next_node
                next_node = head.next
            head.next = prev_node

            return head 

    # Recursively we have:
    """
    def reverseList(self, head: ListNode, prev_node: ListNode) -> ListNode:
        if head.next == None:
            head.next = prev_node
        else:
            reverseList(head.next, head)
    """
