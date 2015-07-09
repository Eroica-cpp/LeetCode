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

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int i = 0;
        int length = nums.size();
        while (i < length) {
            if (nums[i] == target) break;
            i ++;
        }
        return i < length ? i : -1;
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    int a[5] = {1,2,3,4,5};
    vector<int> v (a, a+5);
    Solution s;
    cout << s.search(v, 10) << endl;
    return 0;
}