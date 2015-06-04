#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 4, 2015
# Question: 071-Simplify-Path
# Link:     https://leetcode.com/problems/simplify-path/
# ==============================================================================
# Given an absolute path for a file (Unix-style), simplify it.
# 
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.
# 
# Corner Cases:
# 
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# 
# Another corner case is the path might contain multiple slashes '/' together, 
# such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
# ==============================================================================
# Method: Maintain a stack
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        stack = []
        for i in path.split("/"):
            if not i or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return "/"+"/".join(stack)

if __name__ == '__main__':
    path = "/home//foo/"
    path = "/a/./b/../../c/"
    path = "/home/"
    path = "/../"
    print Solution().simplifyPath(path)