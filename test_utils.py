# @author lucasmiranda42
# encoding: utf-8
# module MPIP_Docker_workshop

"""



"""

from hypothesis import strategies as st
from hypothesis.extra.numpy import arrays
from utils import *
import numpy as np


@given(
    to_sort=arrays(
        shape=(10,),
        dtype=int,
        unique=True,
        elements=st.integers(min_value=-50, max_value=50),
    )
)
def test_sort_array(to_sort):
    """Tests the sort_array function, in utils.py"""
    assert sort_array(to_sort) == np.sort(to_sort)


def test_binary_search():
    """Tests the binary_search function, in utils.py"""
    pass


def test_retrieve_element():
    """Tests the retrieve_element function, in utils.py"""
    pass
