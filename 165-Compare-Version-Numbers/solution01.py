#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 2, 2015
# Question: 165-Compare-Version-Numbers
# Link:     https://leetcode.com/problems/compare-version-numbers/
# ==============================================================================
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise 
# return 0.
# 
# You may assume that the version strings are non-empty and contain only digits 
# and the . character. The . character does not represent a decimal point and 
# is used to separate number sequences. For instance, 2.5 is not "two and a half" 
# or "half way to version three", it is the fifth second-level revision of the 
# second first-level revision.
# 
# Here is an example of version numbers ordering:
# 
# 0.1 < 1.1 < 1.2 < 13.37
# ==============================================================================

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
		x = [int(i) for i in version1.split(".")]
		y = [int(i) for i in version2.split(".")]
		x_len = len(x)
		y_len = len(y)
		if x_len > y_len:
			y += [0] * (x_len - y_len)
		else:
			x += [0] * (y_len - x_len)
		for i in range(max(x_len, y_len)):
			if x[i] > y[i]: 
				return 1
			elif x[i] < y[i]:
				return -1
		return 0