#!/usr/bin/python3
"""
Interval variables
"""

# load the libraries
import numpy as np
from cpmpy import *

# Variables
size = 2

start_1 = intvar(1, 9)
end_1 = intvar(1, 9)
interval_1 = intervalvar(start_1, size, end_1, name="interval_1")

start_2 = intvar(1, 9)
end_2 = intvar(1, 9)
interval_2 = intervalvar(start_2, size, end_2, name="interval_2")

print(interval_1)

model = Model(
    NoOverlap([interval_1, interval_2])
)

if model.solve():
    pass
else:
    print("No solution found")
