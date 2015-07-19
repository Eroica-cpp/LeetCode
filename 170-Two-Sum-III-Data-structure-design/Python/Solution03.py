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
Method: hash table
Time Complexity:
- find O(n)
- add O(n)
Space Complexity: O(n)
Note: 
Still TLE in Python implement, even thought this method is given by LeetCode 
official CleanCodeHandbook in Java.
==============================================================================
"""

class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.dic = {}

    # @return nothing
    def add(self, number):
        self.dic[number] = self.dic.get(number)+1 if self.dic.has_key(number) else 1

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        pairs = {}
        for i in self.dic.keys():
            pairs[value-i] = i

        for i in self.dic.keys():
            if pairs.has_key(i) and (pairs[i] != i or self.dic.get(pairs[i]) >= 2):
                return True

        return False

if __name__ == '__main__':
    queue = [1,4,2,8,5,7]
    tmp = TwoSum()
    while queue:
        tmp.add(queue.pop(0))

    print tmp.dic
    print tmp.find(5)