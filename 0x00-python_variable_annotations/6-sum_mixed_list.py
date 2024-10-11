#!/usr/bin/env python3
""" function type annotations"""


from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """ type-annotated function sum_list which takes a list input_list of
    floats as argument and returns their sum as a float."""
    return float(sum(mxd_lst))
