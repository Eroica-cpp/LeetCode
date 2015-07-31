// ==============================================================================
// Author:   Tao Li (taoli@ucsd.edu)
// Date:     Jul 31, 2015
// Question: 125-Valid-Palindrome
// Link:     https://leetcode.com/problems/valid-palindrome/
// ==============================================================================
// Given a string, determine if it is a palindrome, considering only 
// alphanumeric characters and ignoring cases.

// For example,
// "A man, a plan, a canal: Panama" is a palindrome.
// "race a car" is not a palindrome.

// Note:
// Have you consider that the string might be empty? This is a good question 
// to ask during an interview.

// For the purpose of this problem, we define empty string as valid palindrome.
// ==============================================================================
// Method: Two passes
// Time Complexity: O(n)
// Space Complexity: O(n)
// ==============================================================================

#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> v;

        for (auto c : s)
            if (isalpha(c) || isdigit(c))
                v.push_back(c);

        for (int i = 0; i < v.size()/2; i ++)
            if (tolower(v[i]) != tolower(v[v.size()-i-1]))
                return false;

        return true;
    }
};
