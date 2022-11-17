"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.

Time: O(m * n)
Space: O(1)
"""
from typing import List
import unittest


def zero_matrix(matrix: List[List[int]]) -> None:
    # O(1)
    row_length, col_length = len(matrix), len(matrix[0])
    rowZero = False

    # determine which rows/cols need to be zero
    for r in range(row_length):
        for c in range(col_length):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0  # set the first element in that row to 0
                else:
                    rowZero = True  # if it's the first row

    for r in range(1, row_length):
        for c in range(1, col_length):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(row_length):
            matrix[r][0] = 0

    if rowZero:
        for c in range(col_length):
            matrix[0][c] = 0

    return matrix


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
