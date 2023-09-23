from utils.grid.grid2d import adj_coords_2d

sample = {(0, 2): 7, (1, 2): 8, (2, 2): 9,
          (0, 1): 4, (1, 1): 5, (2, 1): 6,
          (0, 0): 1, (1, 0): 2, (2, 0): 3}


def test_adj_coords_2d():
    assert {(0, 1), (1, 0), (0, -1), (-1, 0)} == set(adj_coords_2d((0, 0)))
    assert {(-1, 1), (0, 1), (1, 1),
            (-1, 0), (1, 0),
            (-1, -1), (0, -1), (1, -1)} == \
        set(adj_coords_2d((0, 0), diagonals=True))
