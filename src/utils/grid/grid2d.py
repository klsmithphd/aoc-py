from typing import Protocol


class Grid2D(Protocol):
    """A convenience protocol for two-dimensional grids"""

    def width(self):
        """Returns the total number of cells in the horizontal direction"""
        pass

    def height(self):
        """Returns the total number cells in the vertical direction"""
        pass

    def contains(self, pos):
        """Returns True if the `pos` is within the extent of the grid"""

    def value(self, pos):
        """Returns the value of the grid at the position `pos` (a tuple)"""
        pass

    def neighbors4(self, pos):
        """Returns the positions and values of the four nearest (von Neumann)
        neighbors of the position `pos` (a tuple)"""
        pass

    def neighbors8(self, pos):
        """Returns the positions and values of the eight nearest (Moore) 
        neighbors of the position `pos` (a tuple)"""
        pass


def adj_coords_2d(pos, diagonals=False):
    """Returns a list of the coordinates of points adjacent to `pos`
    (a tuple). If `diagonals` is unset or False, the four nearest
    von Neumann neighbors are returned. If `diagonals` is True, the
    eight nearest Moore neighbors are returned."""
    x, y = pos
    if diagonals:
        return [(x-1, y+1), (x, y+1), (x+1, y+1),
                (x-1, y), (x+1, y),
                (x-1, y-1), (x, y-1), (x+1, y-1)]
    else:
        return [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]


def neighbors_2d(grid: Grid2D, pos, diagonals=False):
    """Returns a dict of the neighbor locations (keys) and values of the
    neighbors of `pos` in `grid`. """
    return {loc: grid.value(loc)
            for loc in adj_coords_2d(pos, diagonals)
            if grid.contains(loc)}
