// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Jul 7, 2015
// Question: 231-Power-of-Two
// Link:     https://leetcode.com/problems/power-of-two/
// ==============================================================================
// Given an integer, write a function to determine if it is a power of two.
// ==============================================================================
// Method: bit operation
// ==============================================================================

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n-1)) == 0;
    }
};
