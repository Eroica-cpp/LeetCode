#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 5, 2015
# Question: 093-Restore-IP-Addresses
# Link:     https://leetcode.com/problems/restore-ip-addresses/
# ==============================================================================
# Given a string containing only digits, restore it by returning all possible 
# valid IP address combinations.
# 
# For example:
# Given "25525511135",
# 
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
# ==============================================================================
# Method: DFS
# Time Complexity: Exp
# Space Complexity: Exp
# ==============================================================================

class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        if len(s) < 4 or len(s) > 12:
            return []

        collection = []
        self.dfs(collection, s, "", 4)
        return collection

    def dfs(self, collection, s, addr, leftNum):
        if leftNum <= 1:
            if s != "" and int(s) <= 255 and (s[0] != "0" or s=="0"):
                collection.append(addr+s)
            return

        for i in xrange(3):
            if s[:i+1] != "" and int(s[:i+1]) <= 255 and (s[:i+1][0] != "0" or s[:i+1]=="0"):
                self.dfs(collection, s[i+1:], addr+s[:i+1]+'.', leftNum-1)

        return

if __name__ == '__main__':
    s = "25525511135"
    # s = "0001"
    print Solution().restoreIpAddresses(s)