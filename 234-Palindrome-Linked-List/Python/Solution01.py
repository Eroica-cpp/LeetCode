#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 10, 2015
Question: 234-Palindrome-Linked-List
Link:     https://leetcode.com/problems/palindrome-linked-list/
==============================================================================
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
==============================================================================
Method: use extra space
Time Complexity: O(n)
Space Complexity: O(n)
==============================================================================
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        stack = []
        size = 0
        while head:
            stack.append(head.val)
            size += 1
            head = head.next

        for i in xrange(size/2):
            if stack[i] != stack[-i-1]:
                return False

        return True
