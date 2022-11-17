"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 
"""
import unittest
from typing import List

# Solution 1: Transpose x Reflection
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


# Solution 2: Rotate 4 groups
# Time: O(n x n), or O(m) where m is the number of cells
# Space: O(1)
def rotate_matrix(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]
            print("Top: ", top)

            # bottom left -> top
            matrix[layer][i] = matrix[-i - 1][layer]
            print("Left: ", matrix[-i - 1][layer])
            # bottom right -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            print("Bottom: ", matrix[-layer - 1][-i - 1])
            # top right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            print("Right: ", matrix[i][-layer - 1])
            # top left -> right
            matrix[i][-layer - 1] = top
    return matrix


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        )
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
