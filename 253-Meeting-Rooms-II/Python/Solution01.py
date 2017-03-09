#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 8, 2015
Question: 253-Meeting-Rooms-II
Link:     https://leetcode.com/problems/meeting-rooms-ii/
==============================================================================
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
==============================================================================
Method: use extra space to store meeting times
Time Complexity: O(n)
Space Complexity: O(n)
Note: TLE
==============================================================================
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        maxTime = max([i.end for i in intervals])
        counter = [0] * (maxTime + 1)

        for i in intervals:
            for j in xrange(i.start, i.end + 1):
                counter[j] += 1

        return max(counter)

if __name__ == '__main__':
    intervals = [[0, 30],[5, 10],[15, 20]]
    intervals = [Interval(i[0], i[1]) for i in intervals]
    print Solution().minMeetingRooms(intervals)