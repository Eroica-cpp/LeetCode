#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 22, 2015
Question: 138-Copy-List-with-Random-Pointer
Link:     https://leetcode.com/problems/copy-list-with-random-pointer/
====================================================================================
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a deep copy of the list.
====================================================================================
Method: 
====================================================================================
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        dic = {}
        return self.helper(dic, head)

    def helper(self, dic, head):
        if not head:
            return
        elif dic.get(head):
            return head

        new = RandomListNode(head.label)
        dic[new] = 1
        new.next = self.helper(dic, head.next)
        new.random = self.helper(dic, head.random)
        return new

if __name__ == '__main__':
    head = RandomListNode(1)
    head.next = head
    new = Solution().copyRandomList(head)