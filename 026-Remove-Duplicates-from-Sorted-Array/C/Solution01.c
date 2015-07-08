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

#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int index = 0;
    int i;
    for (i = 0; i < numsSize; i++) {
        if (nums[index] != nums[i]) nums[++index] = nums[i];
    }
    return index + 1;
}

/* Unit Test */
#define N 14
int main(int argc, char const *argv[])
{
    int a[N] = {1,1,1,2,2,3,4,5,6,6,7,7,7,8};
    int i;
    removeDuplicates(a, N);
    for (i = 0; i < N; i++) {
        printf("%d\n", a[i]);
    }
    printf("END\n");
    return 0;
}