#!/usr/bin/python
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
x = [0, 1, 2]
y = [0, 1, 2]
print CubicSpline(x,y).c
print CubicSpline(x,y,bc_type = 'clamped').c
