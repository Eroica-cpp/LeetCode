#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 2, 2015
# Question: 203-Remove-Linked-List-Elements
# Link:     https://leetcode.com/problems/remove-linked-list-elements/
# ==============================================================================
# Remove all elements from a linked list of integers that have value val.
# 
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
# 
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
# ==============================================================================
# Method: Naive method; one pass
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        while ptr and ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return dummy.next
        