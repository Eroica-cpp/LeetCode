#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 5, 2015
# Question: 086-Partition-List
# Link:     https://leetcode.com/problems/partition-list/
# ==============================================================================
# Given a linked list and a value x, partition it such that all nodes less 
# than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the 
# two partitions.
# 
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
# ==============================================================================
# Method: One pass; use extra list
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: Try not use extra space
# ==============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head:
            return head

        less, more = [], []
        while head:
            if head.val < x:
                less.append(head.val)
            else:
                more.append(head.val)
            head = head.next

        dummy = ListNode(0)
        p = dummy
        for i in less+more:
            p.next = ListNode(i)
            p = p.next

        return dummy.next