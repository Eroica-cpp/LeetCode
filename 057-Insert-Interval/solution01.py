#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 30, 2015
# Question: 057-Insert-Interval
# Link:     https://leetcode.com/problems/insert-interval/
# ==============================================================================
# Given a set of non-overlapping intervals, insert a new interval into the 
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their 
# start times.
# 
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
# 
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as 
# [1,2],[3,10],[12,16].
# 
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
# ==============================================================================
# Method: Traverse
# Time Complexity: O(n)
Space Complexity: O(n)
# ==============================================================================

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval

    def insert(self, intervals, newInterval):

        start = newInterval.start
        end = newInterval.end
        res = []

        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(intervals[i].start, start)
                end = max(intervals[i].end, end)
            else:
                res.append(intervals[i])
            i += 1

        res.append(Interval(start, end))
        res += intervals[i:]

        return res

if __name__ == '__main__':
    # intervals = [1,2],[3,5],[6,7],[8,10],[12,16]
    # newInterval = [4,9]

    # intervals = [1,3],[6,9]
    # newInterval = [2,5]

    intervals = [[2,4], [10,12]]
    newInterval = [1,3]

    intervals = [Interval(i[0], i[1]) for i in intervals]
    newInterval = Interval(newInterval[0], newInterval[1])
    for i in Solution().insert(intervals, newInterval):
        print i.start, i.end
