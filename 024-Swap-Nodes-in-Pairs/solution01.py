#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 2, 2015
# Question: 024-Swap-Nodes-in-Pairs
# Link:     https://leetcode.com/problems/swap-nodes-in-pairs/
# ==============================================================================
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Your algorithm should use only constant space. You may not modify the values 
# in the list, only nodes itself can be changed.
# ==============================================================================
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: trick issue of reference of values in python language in case of swapping
# ==============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        p = head

        while p and p.next:
            p.val, p.next.val = p.next.val, p.val
            p = p.next.next

        return head

if __name__ == '__main__':
    # head = [1,2,3,4,5,6,7]
    head = [1,2,3,4]

    p = new = ListNode(0)
    for i in head:
        p.next = ListNode(i)
        p = p.next
    head = new.next

    cur = head
    while cur:
        print cur.val
        cur = cur.next
    print

    cur = Solution().swapPairs(head)
    while cur:
        print cur.val
        cur = cur.next
    print    