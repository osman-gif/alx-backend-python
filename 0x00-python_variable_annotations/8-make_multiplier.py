#!/usr/bin/env python3
""" function type annotations"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """  type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a
    float by multiplier"""

    def multiplyMultiplier(multiplier1: float) -> float:
        """function that multiplies a float by multiplier
        """
        return multiplier1 * multiplier
    return multiplyMultiplier
