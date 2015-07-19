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
Method: use a stack; sort
Time Complexity:
- find O(n logn)
- add O(1)
Space Complexity: O(n)
Note: also TLE in Python ... speechless ...
==============================================================================
"""

class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.stack = []

    # @return nothing
    def add(self, number):
        self.stack.append(number)

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        self.stack.sort()
        low, high = 0, len(self.stack)-1
        
        while low < high:
            lowVal, highVal = self.stack[low], self.stack[high]
            if lowVal + highVal == value:
                return True
            elif lowVal + highVal < value:
                low += 1
            else:
                high -= 1

        return False

if __name__ == '__main__':
    queue = [1,4,2,8,5,7]
    tmp = TwoSum()
    while queue:
        tmp.add(queue.pop(0))

    print tmp.stack
    print tmp.find(7)