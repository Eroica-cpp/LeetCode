#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 19, 2015
Question: 170-Two-Sum-III-Data-structure-design
Link:     https://leetcode.com/problems/two-sum-iii-data-structure-design/
==============================================================================
Design and implement a TwoSum class. It should support the following operations: 
add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
==============================================================================
Method: sorted doubly linked list
Time Complexity:
- find O(n)
- add O(n)
Space Complexity: O(n)
Note: TLE in python ...
==============================================================================
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.last = None
        self.next = None

class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.dummy = ListNode(-float('inf'))

    # @return nothing
    def add(self, number):
        p = self.dummy
        last = None
        while p and p.val < number:
            last = p
            p = p.next
        last.next = ListNode(number)
        last.next.next = p
        last.next.last = last
        if p: 
            p.last = last.next

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        head = tail = self.dummy
        while tail.next:
            tail = tail.next

        while head and tail and id(head) != id(tail):
            tmp = head.val + tail.val
            if tmp == value:
                return True
            elif tmp > value:
                tail = tail.last
            else:
                head = head.next

        return False

if __name__ == '__main__':
    tmp = TwoSum()
    queue = [1,3,5]
    while queue:
        tmp.add(queue.pop(0))

    p = tmp.dummy.next
    while p:
        print p.val
        p = p.next

    print tmp.find(4)
    print tmp.find(7)