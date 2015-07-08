/*
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 8, 2015
Question: 026-Remove-Duplicates-from-Sorted-Array
Link:     https://leetcode.com/problems/remove-duplicates-from-sorted-array/
==============================================================================
Given a sorted array, remove the duplicates in place such that each element 
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with 
constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums 
being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
==============================================================================
Method: One pass
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
*/

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int size = nums.size();
        if (size == 0) return 0;
        int index = 0;
        for (int i = 1; i < size; i++) {
            if (nums[index] != nums[i]) nums[++index] = nums[i];
        }
        return index + 1;
    }
};

/* Unit Test */
int main(int argc, char const *argv[])
{
    Solution s;
    int array[] = {1,1,1,2,3,4,4,5};
    vector<int> v(array, array+8) ;
    cout << s.removeDuplicates(v) << endl;
    for (int i = 0; i < v.size(); i++) cout << v[i] << endl;
    return 0;
}