#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 5, 2015
# Question: 092-Reverse-Linked-List-II
# Link:     https://leetcode.com/problems/reverse-linked-list-ii/
# ==============================================================================
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# 
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# 
# return 1->4->3->2->5->NULL.
# 
# Note:
# Given m, n satisfy the following condition:
# 1 <= m <= n <= length of list.
# ==============================================================================
# Method: in-place and in one-pass
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: Verbose code, need to improve
# ==============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        k = m
        while k > 1 and p:
            p = p.next
            k -= 1

        if not p:
            return head

        part1 = p
        p = p.next
        part2 = p

        k = n-m+1
        while k > 1 and p:
            p = p.next
            k -= 1

        if p:
            part3 = p.next
            p.next = None
        else:
            part3 = None

        new_part2 = self.reverseList(part2)

        part1.next = new_part2
        part2.next = part3
        return dummy.next

    def reverseList(self, head):
        if not head:
            return None
        elif not head.next:
            return head
        else:
            lastNode = head.next
            head.next = None
            resList = self.reverseList(lastNode)
            lastNode.next = head
            return resList

if __name__ == '__main__':
    
    lst, m, n = [1,2,3,4,5], 10,5

    head = ListNode(lst[0])
    p = head

    for i in lst[1:]:
        p.next = ListNode(i)
        p = p.next

    new = Solution().reverseBetween(head, m, n)
    p = new

    while p:
        print p.val
        p = p.next