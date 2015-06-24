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
# Method: Iteration without extra space
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: After iterating, set the pointer.next = None !
# ==============================================================================

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
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return

        last = None
        while head:
            tmpNext = head.next
            head.next = last
            last = head
            head = tmpNext

        return last

if __name__ == '__main__':
    lst = [1,2,3,4,5,6,7,8,9]
    lst = [1]

    head = ListNode()
    head.init(lst)
    head.printList()

    new = Solution().reverseList(head)
    new.printList()
