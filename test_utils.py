# @author lucasmiranda42
# encoding: utf-8
# module MPIP_Docker_workshop

"""

Tests for all functions in utils.py

"""

from hypothesis import strategies as st
from hypothesis import given
from utils import *


@given(
    to_sort=st.lists(
        min_size=0,
        max_size=50,
        unique=False,
        elements=st.integers(min_value=-50, max_value=50),
    )
)
def test_sort_array(to_sort):
    """Tests the sort_array function, in utils.py"""
    assert sort_array(to_sort) == sorted(to_sort)


@given(
    to_sort=st.lists(
        min_size=0,
        max_size=50,
        unique=False,
        elements=st.integers(min_value=-50, max_value=50),
    ),
    x=st.integers(min_value=-50, max_value=50),
)
def test_binary_search(to_sort, x):
    """Tests the binary_search function, in utils.py"""

    sorted_list = sorted(to_sort)

    if x in sorted_list:
        assert binary_search(sorted_list, x) <= len(sorted_list)
    else:
        assert binary_search(sorted_list, x) == -1
