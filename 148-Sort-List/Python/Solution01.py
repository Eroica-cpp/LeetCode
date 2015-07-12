#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 12, 2015
Question: 148-Sort-List
Link:     https://leetcode.com/problems/sort-list/
====================================================================================
Sort a linked list in O(n log n) time using constant space complexity.
====================================================================================
Method: merge sort; recursion
Time Complexity: O(n logn)
Space Complexity: O(1)
====================================================================================
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next: return head

        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        fast = slow
        slow = slow.next
        fast.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        dummy = ListNode(-float('inf'))
        p = dummy
        while l1 or l2:
            val1 = l1.val if l1 else float('inf')
            val2 = l2.val if l2 else float('inf')
            if val1 <= val2:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        return dummy.next
