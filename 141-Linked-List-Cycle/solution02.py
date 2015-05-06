#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 6, 2015
# Question: 141-Linked-List-Cycle
# Link:     https://leetcode.com/problems/linked-list-cycle/
# ==============================================================================
# Given a linked list, determine if it has a cycle in it.
# 
# Follow up:
# Can you solve it without using extra space?
# ==============================================================================
# Method: Fast & Slow Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            if id(p1) == id(p2):
                return True
        return False

if __name__ == '__main__':
    head = ListNode(0)
    head.next = head
    # head.next = ListNode(1)
    # head.next.next = ListNode(2)
    print Solution().hasCycle(head)