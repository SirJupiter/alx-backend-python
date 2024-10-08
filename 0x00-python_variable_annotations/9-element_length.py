#!/usr/bin/env python3
"""Annotate function parameters"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate function parameters"""
    return [(i, len(i)) for i in lst]
