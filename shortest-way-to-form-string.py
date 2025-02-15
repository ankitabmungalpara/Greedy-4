"""

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 
Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

1 <= source.length, target.length <= 1000
source and target consist of lowercase English letters.


Time Complexity: O(m * n), where m is the length of the source string and n is the length of the target string. The outer loop iterates over the target, and the inner loop iterates over the source.
Space Complexity: O(1), The solution only uses a few integer variables for indexing and counting, so the space complexity is constant.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach:
# The approach tries to match characters from 'source' to 'target' in a sequential manner. 
# For each traversal of 'source', we incrementally build the subsequences of 'target' until all characters are matched. 
# The process is repeated until all characters of 'target' are covered, returning the minimum number of subsequences required.


class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        target_idx, res = 0, 0

        while target_idx < len(target) :
            prev_idx = target_idx

            for ch in source:
                if target_idx < len(target) and target[target_idx] == ch:
                    target_idx += 1

            if prev_idx == target_idx:
                return -1

            res += 1

        return res

