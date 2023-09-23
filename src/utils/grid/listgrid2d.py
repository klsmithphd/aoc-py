from utils.grid.grid2d import Grid2D, adj_coords_2d, neighbors_2d


class ListGrid2D(Grid2D):
    """A Grid2D backed by a list-of-lists."""

    def __init__(self, l):
        self.__grid = l
        self.__height = len(l)
        self.__width = len(l[0])

    def __eq__(self, other):
        return self.__grid == other._ListGrid__grid

    def contains(self, pos):
        x, y = pos
        return (0 <= x < self.__width) and (0 <= y < self.__height)

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def value(self, pos):
        x, y = pos
        return self.__grid[y][x]

    def neighbors4(self, pos):
        return neighbors_2d(self, pos)

    def neighbors8(self, pos):
        return neighbors_2d(self, pos, diagonals=True)


def strings_to_ListGrid(charmap, strings):
    """Returns a new ListGrid instance formed by converting characters
    in a string into values in the grid. `charmap` is a function of a 
    single character that converts the character into a value useful to
    your problem."""
    def converter(line): return [charmap(c) for c in line]

    return ListGrid2D([converter(line) for line in strings])
