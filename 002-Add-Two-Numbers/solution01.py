#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 11, 2015
# Question: 002-Add-Two-Numbers
# Link:     https://leetcode.com/problems/add-two-numbers/
# ==============================================================================
# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain 
# a single digit. Add the two numbers and return it as a linked list.
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# ==============================================================================
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: Pay attention to the case that l1 and l2 is None while flag is 1
# ==============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        p = ListNode(0)
        head = p
        flag = 0

        while l1 or l2 or flag:
            if l1 and l2:
                p.next = ListNode((l1.val+l2.val+flag)%10) 
                flag = (l1.val+l2.val+flag)/10
                p = p.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                p.next = ListNode((l1.val+flag)%10)
                flag = (l1.val+flag)/10
                p = p.next
                l1 = l1.next
            elif l2:
                p.next = ListNode((l2.val+flag)%10)
                flag = (l2.val+flag)/10
                p = p.next
                l2 = l2.next
            else:
                p.next = ListNode(flag)
                flag = 0

        return head.next

if __name__ == '__main__':
    l1 = ListNode(5)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)

    l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    head = Solution().addTwoNumbers(l1, l2)
    while head:
        print head.val
        head = head.next
