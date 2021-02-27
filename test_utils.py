# @author lucasmiranda42
# encoding: utf-8
# module MPIP_Docker_workshop

"""

Tests for all functions in utils.py

"""

from hypothesis import strategies as st
from hypothesis import given
from hypothesis.extra.numpy import arrays
from utils import *
import numpy as np


@given(
    to_sort=arrays(
        shape=st.integers(min_value=0, max_value=50),
        dtype=int,
        unique=False,
        elements=st.integers(min_value=-50, max_value=50),
    )
)
def test_sort_array(to_sort):
    """Tests the sort_array function, in utils.py"""
    assert np.all(sort_array(to_sort) == np.sort(to_sort))


@given(
    to_sort=arrays(
        shape=st.integers(min_value=0, max_value=50),
        dtype=int,
        unique=False,
        elements=st.integers(min_value=-50, max_value=50),
    ),
    x=st.integers(min_value=-50, max_value=50),
)
def test_binary_search(to_sort, x):
    """Tests the binary_search function, in utils.py"""
    sorted = np.sort(to_sort)

    if x in sorted:
        assert binary_search(sorted, x) < len(sorted)
    else:
        assert binary_search(sorted, x) == -1
