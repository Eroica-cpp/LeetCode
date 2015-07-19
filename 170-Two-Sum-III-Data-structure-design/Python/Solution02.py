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
Method: use python build-in data structure - list
Time Complexity:
- find O(n)
- add O(n)
Space Complexity: O(n)
==============================================================================
"""

class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.items = []

    # @return nothing
    def add(self, number):
        if not self.items: 
            self.items.append(number)
        else:
            i, size = 0, len(self.items)
            while i < size and number > self.items[i]:
                i += 1
            self.items = self.items[:i] + [number] + self.items[i:]

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        low, high = 0, len(self.items)-1
        
        while low < high:
            tmp = self.items[low] + self.items[high]
            if tmp == value:
                return True
            elif tmp < value: 
                low += 1
            else: 
                high -= 1

        return False

if __name__ == '__main__':
    queue = [1,4,2,8,5,7]
    tmp = TwoSum()
    while queue:
        tmp.add(queue.pop(0))

    print tmp.items
    print tmp.find(16)