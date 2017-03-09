/*
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 14, 2015
Question: 038-Count-and-Say
Link:     https://leetcode.com/problems/count-and-say/
==============================================================================
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
==============================================================================
*/

#include <string>
#include <sstream>
#include <iostream>

using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        string s("1");
        while (n--)
            // s = getNext(s);
        return s;
    }

// private:
//     string getNext(string &s) {
//         stringstream ss;
//         return 
//     }
};

/* Unit Test */
int main(int argc, char const *argv[])
{
    stringstream ss;
    string s;
    ss << 10;
    ss >> s;
    return 0;
}