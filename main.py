# @author lucasmiranda42
# encoding: utf-8
# module MPIP_Docker_workshop

"""

Main runfile for the MPIP Docker workshop

"""

import numpy as np
from utils import sort_array, binary_search

example_array = np.random.uniform(-10, 10, 10).astype(int)
sorted = sort_array(example_array)

print("initial array:", example_array)

x = np.random.uniform(-10, 10, 1).astype(int)[0]

print(
    "The randomly generated value {} is{} in the array".format(
        x, ("" if binary_search(sorted, x) != -1 else " not")
    )
)
