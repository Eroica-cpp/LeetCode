#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 26, 2015
Question: 072-Edit-Distance
Link:     https://leetcode.com/problems/edit-distance/
==============================================================================
Given two words word1 and word2, find the minimum number of steps required to 
convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
==============================================================================
Method: DP
Time Complexity: O(n^2)
Space Complexity: O(n^2)
Note: 
1. Reference: http://www.cnblogs.com/lihaozy/archive/2012/12/31/2840152.html
2. EDIT[i, j] = min(EDIT[i-1,j]+1, EDIT[i,j-1]+1, EDIT[i-1,j-1]+f(x[i],y[i]))
3. thought AC, I am still confused with the exchange case, say "ba" -> "ab"
==============================================================================
"""

class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        size1, size2 = len(word1), len(word2)
        dp = [[0]*(size2+1) for _ in xrange(size1+1)]

        for i in xrange(1,size1+1):
            dp[i][0] = i

        for j in xrange(1, size2+1):
            dp[0][j] = j

        for i in xrange(1,size1+1):
            for j in xrange(1,size2+1):
                notSame = int(word1[i-1] != word2[j-1])
                dp[i][j] = min(dp[i-1][j-1]+notSame, min(dp[i-1][j]+1, dp[i][j-1]+1))

        return dp[-1][-1]

if __name__ == '__main__':
    word1, word2 = "abc", "cba"
    print Solution().minDistance(word1, word2)