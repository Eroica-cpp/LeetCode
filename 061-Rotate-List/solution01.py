#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 4, 2015
# Question: 061-Rotate-List
# Link:     https://leetcode.com/problems/rotate-list/
# ==============================================================================
# Given a list, rotate the list to the right by k places, where k is non-negative.
# 
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
# ==============================================================================

# ==============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head:
            return None

        p = head
        n = 0
        end = ListNode(0)
        while p:
            end = p
            p = p.next
            n += 1

        k %= n
        if k == 0:
            return head

        dummy = ListNode(0)
        p = head
        i = n-k-1
        while i > 0:
            p = p.next
            i -= 1

        dummy.next = p.next
        p.next = None
        end.next = head

        return dummy.next

if __name__ == '__main__':
    k = 0
    lst = [1,2,3,4,5]
    head = ListNode(0)
    p = head
    for i in lst:
        p.next = ListNode(i)
        p = p.next
    head = head.next

    p = head
    while p:
        print p.val
        p = p.next

    new = Solution().rotateRight(head, k)

    print
    p = new
    while p:
        print p.val
        p = p.next