#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 6, 2015
# Question: 141-Linked-List-Cycle
# Link:     https://leetcode.com/problems/linked-list-cycle/
# ==============================================================================
# Given a linked list, determine if it has a cycle in it.
# 
# Follow up:
# Can you solve it without using extra space?
# ==============================================================================
# Method: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: Use node's address, id(obj) as its identifier, rather than 
# node's value, head.val
# ==============================================================================

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        dic = {}
        while head:
            if dic.get(id(head)):
                return True
            else:
                dic[id(head)] = head
                head = head.next
        return False

if __name__ == '__main__':
    head = ListNode(0)
    head.next = head
    print Solution().hasCycle(head)