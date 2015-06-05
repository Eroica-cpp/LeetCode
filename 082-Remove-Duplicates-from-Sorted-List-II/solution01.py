#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 4, 2015
# Question: 082-Remove-Duplicates-from-Sorted-List-II
# Link:     https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# ==============================================================================
# Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
# ==============================================================================
# Method: Two pointers
# ==============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head

        dummy = ListNode(float('inf'))
        dummy.next = head
        new = dummy
        p = head
        lastVal = -float('inf')

        while p and p.next:
            if p.val != lastVal and p.val != p.next.val:
                new.next = p
                new = new.next
            lastVal = p.val
            p = p.next

        if p.val != lastVal:
            new.next = p
            new.next.next = None
        else:
            new.next = None

        return dummy.next

if __name__ == '__main__':
    lst = [1,1,1,2,3,3,4,5,5,5,9,9]
    lst = [1,1,1]

    head = ListNode(lst[0])
    p = head
    for i in lst[1:]:
        p.next = ListNode(i)
        p = p.next

    new = Solution().deleteDuplicates(head)
    p = new
    while p:
        print p.val
        p = p.next