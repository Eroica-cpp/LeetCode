#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 5, 2015
# Question: 206-Reverse-Linked-List
# Link:     https://leetcode.com/problems/reverse-linked-list/
# ==============================================================================
# Reverse a singly linked list.
# 
# click to show more hints.
# 
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
# ==============================================================================
# Method: Iteration
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: After iterating, set the pointer.next = None !
# ==============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        while self:
            print self.val
            self = self.next
        print

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return None
        stack = []
        while head:
            stack.append(head)
            head = head.next
        newHead = stack.pop()
        ptr = newHead
        while stack:
            ptr.next = stack.pop()
            ptr = ptr.next
        ptr.next = None
        return newHead

if __name__ == '__main__':
    head = ListNode(1)
    p = head
    p.next = ListNode(2)
    p.next.next = ListNode(3)
    p.next.next.next = ListNode(4)
    p.next.next.next.next = ListNode(5)    
    head.printList()
    Solution().reverseList(head).printList()