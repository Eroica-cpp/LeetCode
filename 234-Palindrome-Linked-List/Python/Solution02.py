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
Method: find middle point, then reverse the rest linked list. Finally traverse
the two parts at the same time.
Time Complexity: O(n)
Space Complexity: O(1)
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
        if not head: return True
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        last = None
        while p1:
            tmp = p1.next
            p1.next = last
            last = p1
            p1 = tmp

        while head and last:
            if head.val != last.val: return False
            head = head.next
            last = last.next

        return True
