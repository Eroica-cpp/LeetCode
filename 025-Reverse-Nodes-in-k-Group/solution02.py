#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 24, 2015
Question: 025-Reverse-Nodes-in-k-Group
Link:     https://leetcode.com/problems/reverse-nodes-in-k-group/
==============================================================================
Given a linked list, reverse the nodes of a linked list k at a time and return 
its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end 
should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
==============================================================================
Method: use only constant memory
Time Complexity: O(n)
Space Complexity: O(1)
Note: reference feature of python is somtimes confusing
==============================================================================
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

    def init(self, lst):
        if not lst:
            return
        lst.reverse()
        self.val = lst.pop()
        p = self
        while lst:
            p.next = ListNode(lst.pop())
            p = p.next

    def printList(self):
        p = self
        stack = []
        while p:
            stack.append(p.val)
            p = p.next
        print stack

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        p1 = head
        p2 = dummy
        while p1:
            i = k
            while p1 and i > 0:
                p1 = p1.next
                i -= 1
            if i > 0:
                break
            last = p1
            tmp = p2.next
            j = k
            while j > 0:
                tmpNext = tmp.next
                tmp.next = last
                last = tmp
                tmp = tmpNext
                j -= 1
            p2.next = last
            while p2.next != p1:
                p2 = p2.next

        return dummy.next

if __name__ == '__main__':
    lst, k = [1,2,3,4,5,6,7,8,9,10,11,12], 3
    lst, k = [1,2,3,4], 2

    head = ListNode()
    head.init(lst)
    head.printList()

    new = Solution().reverseKGroup(head, k)
    new.printList()
