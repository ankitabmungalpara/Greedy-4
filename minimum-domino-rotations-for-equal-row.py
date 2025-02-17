"""

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 
Example 1:

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6


Time Complexity: O(N) – iterated through the list at most twice, making it linear.
Space Complexity: O(1) – used only a few extra variables, so space remains constant.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach:
# it checks if it's possible to make all dominoes show the same number by choosing either tops[0] or bottoms[0] as the target.  
# It iterates through the array, counting mismatches where swaps are required, and returns the minimum swaps needed.  
# If neither number can be made uniform across all dominoes, it returns -1.  


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        for target in [tops[0], bottoms[0]]:
            missT, missB = 0, 0
            for i in range(len(tops)):
                if not (tops[i] == target or bottoms[i] == target):
                    break
                if tops[i] != target: 
                    missT += 1
                if bottoms[i] != target:
                    missB += 1

                if i == len(tops) - 1:
                    return min(missT, missB)

        return -1


