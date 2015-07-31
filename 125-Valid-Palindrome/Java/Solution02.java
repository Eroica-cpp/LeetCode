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
// Method: One pass
// Time Complexity: O(n)
// Space Complexity: O(1)
// ==============================================================================

import java.lang.*;
import java.util.*;

public class Solution02 {
    public static boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            while (i < j && !Character.isLetterOrDigit(s.charAt(i))) i ++;
            while (i < j && !Character.isLetterOrDigit(s.charAt(j))) j --;
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) return false;
            i ++; j --;
        }
        return true;
    }

    public static void main(String[] args) {
        String s = new String("121");
        System.out.println(isPalindrome(s));
    }
}