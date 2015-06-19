#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 19, 2015
# Question: 142-Linked-List-Cycle-II
# Link:     https://leetcode.com/problems/linked-list-cycle-ii/
# ==============================================================================
# Given a linked list, return the node where the cycle begins. If there is no 
# cycle, return null.

# Follow up:
# Can you solve it without using extra space?
# ==============================================================================
# Method: Use extra space
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        dic = {}
        while head:
            if dic.get(id(head)):
                return head
            else:
                dic[id(head)] = 1
                head = head.next
        return
