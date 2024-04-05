# python std library
import unittest
from collections import deque
from typing import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        max_row_idx = n // 2
        row_idx = 0
        while row_idx < max_row_idx:
            edge = n - row_idx - 1
            for col_idx in range(row_idx, edge):
                edge_mod = edge - col_idx * 1 + row_idx
                top_left = matrix[row_idx][col_idx]
                top_right = matrix[col_idx][edge]
                btm_right = matrix[edge][edge_mod]
                btm_left = matrix[edge_mod][row_idx]

                matrix[row_idx][col_idx] = btm_left
                matrix[col_idx][edge] = top_left
                matrix[edge][edge_mod] = top_right
                matrix[edge_mod][row_idx] = btm_right
            row_idx += 1


class testMatrices(unittest.TestCase):
    def test_case_rotate_in_memory_a(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        expected_output = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11],
        ]
        Solution().rotate(matrix)
        assert expected_output == matrix
