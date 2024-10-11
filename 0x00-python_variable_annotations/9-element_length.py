#!/usr/bin/env python3
""" function type annotations"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ annotated this function from:
    def element_length(lst):
    return [(i, len(i)) for i in lst]"""
    return [(i, len(i)) for i in lst]
