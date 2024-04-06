# python std library
import unittest
from typing import *


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        from math import comb

        data = [[1]]
        idx = 1
        while idx < numRows:
            row_data = []
            for k in range(idx):
                row_data.append(comb(idx, k))
            row_data.append(1)
            data.append(row_data)
            idx += 1
        return data


class testDyanmicProgramming(unittest.TestCase):
    def test_pascals_triangle(self):
        numRows = 5
        soln = Solution().generate(numRows)
        expected_output = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1 ]]
        assert soln == expected_output