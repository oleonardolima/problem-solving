## Problem Statement: https://leetcode.com/problems/add-two-numbers/
## TODO: Improve solution for better readability :)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        tmp = 0
        first_pass = True
        l3 = ListNode(0)
        prev_node = ListNode(0)

        # 1st Case: both lists have a single element
        while True:
            sum = l1.val + l2.val + tmp
            if tmp > 0:
                tmp = 0
            if (sum >= 10):
                if (sum == 10):
                    tmp = 1
                    sum = 0
                else:
                    sum = sum - 10
                    tmp = 1
            if first_pass:
                l3 = ListNode(sum)
                prev_node = l3
                first_pass = False
            else:    
                node = ListNode(sum)
                prev_node.next = node
                prev_node = node

            if (l1.next == None or l2.next == None):
                break
            #print(sum)
            l1 = l1.next
            l2 = l2.next

        if not (l1.next != None and l2.next != None):
            if (l1.next != None):
                while (l1.next != None):
                    #print(l1)
                    l1 = l1.next
                    sum = l1.val + tmp
                    if tmp > 0:
                        tmp = 0
                    if (sum >= 10):
                        if (sum == 10):
                            tmp = 1
                            sum = 0
                        else:
                            sum = sum - 10
                            tmp = 1
                    node = ListNode(sum)
                    prev_node.next = node
                    prev_node = node
            if (l2.next != None):
                while (l2.next != None):
                    #print(l2)
                    l2 = l2.next
                    sum = l2.val + tmp
                    if tmp > 0:
                        tmp = 0
                    if (sum >= 10):
                        if (sum == 10):
                            tmp = 1
                            sum = 0
                        else:
                            sum = sum - 10
                            tmp = 1
                    node = ListNode(sum)
                    prev_node.next = node
                    prev_node = node
        else:
            sum = l1.val + l2.val + tmp
            if tmp > 0:
                tmp = 0
            if (sum >= 10):
                if (sum == 10):
                    tmp = 1
                    sum = 0
                else:
                    sum = sum - 10
                    tmp = 1
            node = ListNode(sum)
            prev_node.next = node
            prev_node = node

        if tmp > 0:
                node = ListNode(tmp)
                prev_node.next = node
                prev_node = node

        return l3