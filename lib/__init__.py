
"""
lib/__init__.py
Procedural generation utilities for 2D maps, mazes, and general grid logic.
"""

# 2D grid/map/maze utilities
from . import *

import random

def empty_grid(width, height, fill=0):
	"""Create a 2D grid (list of lists) filled with a value."""
	return [[fill for _ in range(width)] for _ in range(height)]

def print_grid(grid):
	"""Print a 2D grid to the console."""
	for row in grid:
		print(''.join(str(cell) for cell in row))

def random_point(width, height):
	"""Return a random (x, y) point within the grid bounds."""
	return random.randint(0, width-1), random.randint(0, height-1)

def neighbors(x, y, width, height, diagonals=False):
	"""Yield neighbor coordinates for a cell in a 2D grid."""
	for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
		nx, ny = x+dx, y+dy
		if 0 <= nx < width and 0 <= ny < height:
			yield nx, ny
	if diagonals:
		for dx, dy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
			nx, ny = x+dx, y+dy
			if 0 <= nx < width and 0 <= ny < height:
				yield nx, ny