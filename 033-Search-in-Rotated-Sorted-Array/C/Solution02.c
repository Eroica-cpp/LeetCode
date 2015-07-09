/*
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 9, 2015
Question: 033-Search-in-Rotated-Sorted-Array
Link:     https://leetcode.com/problems/search-in-rotated-sorted-array/
==============================================================================
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its 
index, otherwise return -1.

You may assume no duplicate exists in the array.
==============================================================================
Method: brute force
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
*/

int search(int* nums, int numsSize, int target) {
    int i;
    for (i = 0; i < numsSize; i ++) {
        if (nums[i] == target) return i;
    }
    return -1;
}

/* Unit Test */
int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}