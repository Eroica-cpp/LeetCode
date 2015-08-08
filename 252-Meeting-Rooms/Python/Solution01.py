#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 8, 2015
Question: 252-Meeting-Rooms
Link:     https://leetcode.com/problems/meeting-rooms/
==============================================================================
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
==============================================================================
Method: sort first; trivial
Time Complexity: O(n log n)
Space Complexity: O(1)
==============================================================================
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {boolean}
    def canAttendMeetings(self, intervals):
        size = len(intervals)
        if size <= 1: return True

        intervals.sort(key=lambda x: x.start)
        for i in xrange(size - 1):
            if intervals[i+1].start < intervals[i].end: return False

        return True

if __name__ == '__main__':
    intervals = [[0, 30],[5, 10],[15, 20]]
    intervals = [Interval(i[0], i[1]) for i in intervals]
    print Solution().canAttendMeetings(intervals)